# django_users
a django app that provides basic user functionality, as a foundation for other apps.

## install
pip install git+https://github.com/millerthegorilla/django_users.git#egg=django_users
add django_users and django_email_verification to your installed apps.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'django_users',
    'django_email_verification',  # you have to add this
]
```

## settings
You will need to set the settings.BASE_HTML for the statement `{% extends BASE_HTML %}` in the templates where BASE_HTML comes from the context_processor.  The standard django_auth settings are useful as well:
```
LOGIN_REDIRECT_URL = reverse_lazy('posts')
LOGOUT_REDIRECT_URL = reverse_lazy('landing_page')
LOGIN_URL = reverse_lazy('login')
```
The following settings are for [django_email_verification](https://github.com/LeoneBacciu/django-email-verification) which adds the ability to send token confirmation emails.
You have to add these parameters to the settings, you have to include all of them except the last one:

```python
def verified_callback(user):
    user.is_active = True


EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'mail_body.html'
EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'
EMAIL_MULTI_USER = True  # optional (defaults to False)

# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mymail@gmail.com'
EMAIL_HOST_PASSWORD = 'mYC00lP4ssw0rd'  # os.environ['password_key'] suggested
EMAIL_USE_TLS = True
```

In detail:

+ `EMAIL_VERIFIED_CALLBACK`: the function that will be called when the user successfully verifies the email. Takes the
  user object as argument.
+ `EMAIL_FROM_ADDRESS`: this can be the same as `EMAIL_HOST_USER` or an alias address if required.
+ `EMAIL_MAIL_`:
    * `SUBJECT`: the mail default subject.
    * `HTML`: the mail body template in form of html.
    * `PLAIN`: the mail body template in form of .txt file.
+ `EMAIL_TOKEN_LIFE`: the lifespan of the email link (in seconds).
+ `EMAIL_PAGE_TEMPLATE`: the template of the success/error view.
+ `EMAIL_PAGE_DOMAIN`: the domain of the confirmation link (usually your site's domain).
+ `EMAIL_MULTI_USER`: (optional) if `True` an error won't be thrown if multiple users with the same email are present (just one will be activated)

You will also need recaptcha settings...
```
## RECAPTCHA SETTINGS
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
```
The keys shown here are the test keys that allow you to use the recaptcha in your development setup.  The silenced system check simply silences the warning that is displayed that says that the recaptcha keys are the test keys.

## dependencies
django-crispy-forms==1.11.2
django-email-verification==0.1.0
django-password-validators==1.4.0
django-recaptcha==2.0.6
