import os
from collections import OrderedDict
import importlib

from django.apps import apps, AppConfig
from django.conf import settings
from django.core.management import call_command

from crispy_forms import templates as crispy_templates
from crispy_bootstrap5 import templates as bs5_templates
from captcha import templates as captcha_templates


my_apps = [
    {"name": "crispy_forms", "templates": crispy_templates},
    {"name": "crispy_bootstrap5", "templates": bs5_templates},
    {"name": "captcha", "templates": captcha_templates},
    {"name": "django_email_verification", "templates": ""},
]


class DjangoUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_users"

    def ready(self) -> None:
        global my_apps
        try:
            if not settings.TOPLEVELCONFIG:
                settings.TOPLEVELCONFIG = self.__class__
                self.populate_my_apps()
                self.install_apps()
        except AttributeError:
            settings.TOPLEVELCONFIG = self.__class__
            self.populate_my_apps()
            self.install_apps()

    def populate_my_apps(self):
        global my_apps
        for app in my_apps:
            try:
                theapp = importlib.import_module(app["name"] + ".apps")
                my_apps += [app for app in theapp.my_apps if app not in my_apps]
                app["setup"] = theapp.setup_apps
            except (ModuleNotFoundError, AttributeError):
                pass

    def install_apps(self):
        for app in my_apps:
            if app["name"] not in settings.INSTALLED_APPS:
                settings.INSTALLED_APPS += (app["name"],)
                apps.app_configs = OrderedDict()
                apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False
                apps.clear_cache()
                apps.populate(settings.INSTALLED_APPS)
                if app["templates"] != "":
                    settings.TEMPLATES[0]["DIRS"].append(
                        os.path.abspath(app["templates"].__path__._path[0])
                    )
                if "setup" in app:
                    app["setup"]()
        # static = os.path.abspath(
        #     importlib.import_module(app["name"]).__path__[0] + "/static/"
        # )
        # if os.path.isdir(static):
        #     sdir = True
        #     settings.STATICFILES_DIRS += [static]

        # if sdir:
        #     call_command("collectstatic", verbosity=0, interactive=False)
        setup_apps()


def setup_apps():
    from django_email_verification import urls as email_urls  # include the urls
    from django import urls

    root_url = importlib.import_module(settings.ROOT_URLCONF)
    if urls.path("email/", urls.include(email_urls)) not in root_url.urlpatterns:
        root_url.urlpatterns.append(
            urls.path("email/", urls.include(email_urls)),
        )
