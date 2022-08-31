from django.shortcuts import reverse
from pytest_django.asserts import assertTemplateUsed

from django_users import forms as user_forms
from django_users import views as user_views


def test_uses_login_template(client):
    response = client.get(reverse("login"))
    assert response.status_code == 200
    assertTemplateUsed(response, "registration/login.html")


def test_uses_profile_template(auto_login_user, active_user):
    client, user = auto_login_user(active_user)
    response = client.get(reverse("profile"))
    assert response.status_code == 200
    assertTemplateUsed(response, "django_users/profile.html")


def test_uses_registration_template(client):
    response = client.get(reverse("register"))
    assert response.status_code == 200
    assertTemplateUsed(response, "django_users/register.html")


def test_register_view(validate_captcha, user_details, db):
    form_data = {
        "username": user_details.username,
        "email": user_details.email,
        "password1": user_details.password,
        "password2": user_details.password,
    }
    _form = user_forms.CustomUserCreation(data=form_data)
    _view = user_views.Register()
    response = _view.form_valid(_form)
    assert response.status_code == 302
    assert response.url == "/accounts/registration_confirmation_sent/"


def test_resend_confirmation_view(validate_captcha, user):
    form_data = {
        "username": user.username,
    }
    _form = user_forms.UserResendConfirmation(data=form_data)
    _view = user_views.ResendConfirmation()
    response = _view.form_valid(_form)
    assert response.status_code == 302
    assert response.url == "/accounts/registration_confirmation_sent/"


def test_confirm_sent(rf):
    _view = user_views.ConfirmSent()
    request = rf.get(reverse("confirmation_sent"))
    response = _view.get(request)
    assert response.status_code == 200
    assert "Email Sent" in response.getvalue().decode()
