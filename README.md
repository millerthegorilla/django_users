# django_users
a django app that provides basic user functionality, as a foundation for other apps.

## install
pip install git+https://github.com/millerthegorilla/safe_imagefield.git#egg=safe_imagefield

## settings
You will need to set the site domain in the admin app, and also the settings.BASE_HTML for the statement `{% extends BASE_HTML %}` in the templates where BASE_HTML comes from the context_processor.

## dependencies
django-crispy-forms==1.11.2
django-email-verification==0.1.0
django-password-validators==1.4.0
django-recaptcha==2.0.6
