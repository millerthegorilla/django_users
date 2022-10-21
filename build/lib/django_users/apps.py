import os
from collections import OrderedDict
import importlib

from django.apps import apps, AppConfig
from django.conf import settings

from crispy_forms import templates as crispy_templates
from crispy_bootstrap5 import templates as bs5_templates
from captcha import templates as captcha_templates


APPS = [
    {"name": "crispy_forms", "templates": crispy_templates},
    {"name": "crispy_bootstrap5", "templates": bs5_templates},
    {"name": "captcha", "templates": captcha_templates},
    {"name": "django_email_verification", "templates": ""},
]


class DjangoUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_users"

    def ready(self) -> None:
        for app in APPS:
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
        from django_email_verification import urls as email_urls  # include the urls
        from django import urls

        root_url = importlib.import_module(settings.ROOT_URLCONF)
        if urls.path("email/", urls.include(email_urls)) not in root_url.urlpatterns:
            root_url.urlpatterns.append(
                urls.path("email/", urls.include(email_urls)),
            )
