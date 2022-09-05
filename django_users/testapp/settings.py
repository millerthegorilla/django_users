"""
Django settings for django_users_test_project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django import urls

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# for context processor
BASE_HTML = "django_users/base.html"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)6g^go@h2l@@xf+8hqhezr0hrmqvi-j$pgy6!*(n@^rx#y!54-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "django_users",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "captcha",
    "django_email_verification",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_users.testapp.urls"
LOGIN_URL = urls.reverse_lazy("login")
LOGIN_REDIRECT_URL = urls.reverse_lazy("profile")
STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_users.context_processors.base_html",
                "django_users.context_processors.siteName",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mem_db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DJANGO-EMAIL-VERIFICATION SETTINGS
def verified_callback(user):
    user.is_active = True


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"  # "django.core.mail.backends.console.EmailBackend"  # noqa: E501
EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_ACTIVE_FIELD = "is_active"
EMAIL_HOST_USER = "test@django_users.com"
EMAIL_FROM_ADDRESS = "noreply@django_users.com"
EMAIL_MAIL_SUBJECT = "Confirm your email"
EMAIL_MAIL_HTML = "emails/mail_body.html"
EMAIL_MAIL_PLAIN = "emails/mail_body.txt"
EMAIL_MAIL_PAGE_TEMPLATE = "registration/confirm.html"
EMAIL_PAGE_DOMAIN = "http://127.0.0.1:8000"
EMAIL_MAIL_TOKEN_LIFE = 60 * 60 * 24
CUSTOM_SALT = "asdfasdfasdffasdfa234234"

## RECAPTCHA SETTINGS
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

SITE_NAME = "django_users_test_app"
