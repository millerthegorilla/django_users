from django import urls
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import forms as users_forms
from . import views as users_views

app_name = "django_users"

urlpatterns = [
    urls.path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    urls.path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    urls.path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="django_users/resend_form.html",
            form_class=users_forms.UserPasswordReset,
            from_email=settings.EMAIL_FROM_ADDRESS,
            extra_context={"instructions": "Send a password reset link..."},
        ),
        name="password_reset",
    ),
    urls.path(
        "registration_confirmation_sent/",
        users_views.ConfirmSent.as_view(
            template_name="django_users/registration_confirmation_sent.html"
        ),
        name="confirmation_sent",
    ),
    urls.path(
        "resend_confirmation/",
        users_views.ResendConfirmation.as_view(),
        name="resend_confirmation",
    ),
    urls.path("register/", users_views.Register.as_view(), name="register"),
    urls.path("profile/", users_views.Profile.as_view(), name="profile"),
]
