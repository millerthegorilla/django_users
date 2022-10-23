import os
from collections import OrderedDict
import importlib

from django.apps import apps, AppConfig
from django.conf import settings

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
                settings.STATICFILES_DIRS += [
                    os.path.abspath(
                        importlib.import_module(app["name"]).__path__.path[0]
                        + "/static/"
                    )
                ]
                try:
                    theapp = importlib.import_module(app["name"] + ".apps")
                    my_apps += theapp.my_apps
                    theapp.setup_apps()
                except (ModuleNotFoundError, AttributeError):
                    pass
        setup_apps()


def setup_apps():
    from django_email_verification import urls as email_urls  # include the urls
    from django import urls

    root_url = importlib.import_module(settings.ROOT_URLCONF)
    if urls.path("email/", urls.include(email_urls)) not in root_url.urlpatterns:
        root_url.urlpatterns.append(
            urls.path("email/", urls.include(email_urls)),
        )
