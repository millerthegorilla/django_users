import os
import random
import time
from faker import Faker
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from pytest_bdd import then, when

User = get_user_model()

REGISTER_URL = "/accounts/register/"
LOGIN_URL = "/accounts/login/"
PASSWORD_RESET_URL = "/accounts/password_reset/"
RESEND_CONFIRM_URL = "/accounts/resend_confirmation/"

try:
    LANDING_URL = settings.LOGIN_REDIRECT
except AttributeError:
    LANDING_URL = "/accounts/profile/"

    LINKS_DICT = {
        "registration": f"a[href='{REGISTER_URL}']",
        "reset_password": f"a[href='{PASSWORD_RESET_URL}']",
        "resend_confirmation": f"a[href='{RESEND_CONFIRM_URL}']",
    }

    PAGES_DICT = {
        "login": LOGIN_URL,
        "registration": REGISTER_URL,
        "reset_password": PASSWORD_RESET_URL,
        "resend_confirmation": RESEND_CONFIRM_URL,
    }


@pytest.fixture()
def browser(sb, live_server, settings):
    staging_server = os.environ.get("STAGING_SERVER")
    if staging_server:
        sb.visit(staging_server)
    else:
        sb.visit(live_server)
    sb.domain = sb.get_domain_url(sb.get_current_url())
    settings.EMAIL_PAGE_DOMAIN = sb.domain
    sb.pages = PAGES_DICT
    sb.links = LINKS_DICT
    return sb


@pytest.fixture()
def login_page(browser):
    browser.visit(browser.domain + LOGIN_URL)
    return browser


@pytest.fixture()
def landing_page(browser):
    browser.visit(browser.domain + LANDING_URL)
    return browser


@pytest.fixture()
def registration_page(browser):
    browser.visit(browser.domain + REGISTER_URL)
    return browser


@pytest.fixture()
def confirmation_page(browser):
    browser.visit(browser.domain + RESEND_CONFIRM_URL)
    return browser


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


# Shared steps
@then("I should see the username input")
def i_should_see_the_username_input(page):
    """I should see the username box."""
    page.assert_element("#id_username")


@when("clicks on submit button")
def clicks_on_submit_button(page, db):
    """clicks on submit button."""
    page.click('button[type="submit"]')


@pytest.fixture()
def user(
    transactional_db, login_user_details
):  # transactional_db because using live_server
    user = User.objects.create(
        username=login_user_details.username, password=login_user_details.password
    )
    yield user
    user.delete()
