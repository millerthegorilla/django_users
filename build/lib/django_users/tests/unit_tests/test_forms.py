import pytest
from django.forms.models import model_to_dict

from django_users import forms as user_forms


def test_registration_form(validate_captcha, user_details, db):
    form_data = {
        "username": user_details.username,
        "email": user_details.email,
        "password1": user_details.password,
        "password2": user_details.password,
    }
    _form = user_forms.CustomUserCreation(data=form_data)
    assert _form.is_valid()


def test_registration_form_invalid_user(validate_captcha, active_user):
    _form = user_forms.CustomUserCreation(model_to_dict(active_user))
    assert not _form.is_valid()


def test_password_reset_form(validate_captcha, active_user):
    form_data = {"email": active_user.email}
    _form = user_forms.UserPasswordReset(data=form_data)
    assert _form.is_valid()


def test_password_reset_form_inactive_user(validate_captcha, user):
    form_data = {"email": user.email}
    _form = user_forms.UserPasswordReset(data=form_data)
    assert not _form.is_valid()


def test_password_reset_form_invalid_user(validate_captcha, user_details, db):
    form_data = {"email": user_details.email}
    _form = user_forms.UserPasswordReset(data=form_data)
    assert not _form.is_valid()


def test_resend_confirmation_form(validate_captcha, user, db):
    form_data = {"username": user.username}
    _form = user_forms.UserResendConfirmation(data=form_data)
    assert _form.is_valid()


def test_resend_confirmation_form_active_user(validate_captcha, active_user, db):
    form_data = {"username": active_user.username}
    _form = user_forms.UserResendConfirmation(data=form_data)
    assert not _form.is_valid()


def test_resend_confirmation_form_invalid_user(validate_captcha, user_details, db):
    form_data = {"username": user_details.username}
    _form = user_forms.UserResendConfirmation(data=form_data)
    assert not _form.is_valid()
