import random

import captcha
import pytest
from faker import Faker


class UserDetails:
    def __init__(self):
        fake = Faker()
        fake.random.seed(random.randint(0, 999))
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.domain = fake.domain_name()
        self.username = self.first_name + str(random.randint(101, 999))
        self.password = fake.password(14)
        self.email = self.first_name + "_" + self.last_name + "@" + self.domain


@pytest.fixture()
def user_details(faker):
    return UserDetails()


@pytest.fixture()
def user(
    transactional_db, user_details, django_user_model
):  # transactional_db because using live_server
    user = django_user_model.objects.create(
        username=user_details.username,
        password=user_details.password,  # https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests  # noqa: E501
        email=user_details.email,
    )
    user.set_password(user_details.password)
    user.is_active = False
    user.save()
    yield user
    user.delete()


@pytest.fixture()
def active_user(user):
    user.is_active = True
    user.save()
    return user


@pytest.fixture()
def auto_login_user(db, client, user, user_details):
    def make_auto_login(user=None):
        if user is None:
            user = user()
        client.login(username=user_details.username, password=user_details.password)
        return client, user

    return make_auto_login


@pytest.fixture()
def validate_captcha(monkeypatch):
    def val(*args, **kwargs):
        return True

    monkeypatch.setattr(captcha.fields.ReCaptchaField, "validate", val)
    return True
