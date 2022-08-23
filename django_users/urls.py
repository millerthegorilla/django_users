from django import urls
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views

from . import forms as users_forms
from . import views as users_views

urlpatterns = [
    urls.path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
    ),
    urls.path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="django_users/resend_form.html",
            form_class=users_forms.UserPasswordReset,
            extra_context={"instructions": "Send a password reset link..."},
        ),
        name="password_reset",
    ),
    urls.path(
        "accounts/registration_confirmation_sent/",
        users_views.ConfirmSent.as_view(
            template_name="django_users/registration_confirmation_sent.html"
        ),
        name="confirmation_sent",
    ),
    urls.path(
        "accounts/resend_confirmation/",
        users_views.ResendConfirmation.as_view(),
        name="resend_confirmation",
    ),
    urls.path("accounts/register/", users_views.Register.as_view(), name="register"),
    urls.path("accounts/profile/", users_views.Profile.as_view(), name="profile"),
    urls.path("accounts/", urls.include(auth_urls)),
]
