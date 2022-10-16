import os
import time

import pytest
from django.conf import settings
from django.urls import reverse
from pytest_bdd import then, when
from selenium.webdriver.common.by import By

RECAPTCHA_SLEEP_INTERVAL = 3

REGISTER_URL = reverse("django_users:register")
try:
    LANDING_URL = settings.LOGIN_REDIRECT
except AttributeError:
    LANDING_URL = "/accounts/profile/"
CONFIRMATION_URL = reverse("django_users:confirmation_sent")
LOGIN_URL = reverse("django_users:login")
RESEND_CONFIRM_URL = reverse("django_users:resend_confirmation")
PASSWORD_RESET_URL = reverse("django_users:password_reset")
PASSWORD_RESET_DONE_URL = reverse("password_reset_done")
PASSWORD_RESET_CONFIRM_URL = "accounts/reset/Ng/set-password/"
PASSWORD_RESET_COMPLETE_URL = reverse("password_reset_complete")


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
    "password_reset_done": PASSWORD_RESET_DONE_URL,
    "password_reset_confirm": PASSWORD_RESET_CONFIRM_URL,
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
def resend_confirmation_page(browser):
    browser.visit(browser.domain + RESEND_CONFIRM_URL)
    return browser


@pytest.fixture()
def confirmation_page(browser):
    browser.visit(browser.domain + CONFIRMATION_URL)
    return browser


@pytest.fixture()
def reset_password_page(browser):
    browser.visit(browser.domain + PASSWORD_RESET_URL)
    return browser


@pytest.fixture()
def reset_password_done_page(browser):
    browser.visit(browser.domain + PASSWORD_RESET_DONE_URL)
    return browser


@pytest.fixture()
def reset_password_confirm_page(browser):
    browser.visit(browser.domain + PASSWORD_RESET_CONFIRM_URL)
    return browser


@pytest.fixture()
def reset_password_complete_page(browser):
    browser.visit(browser.domain + PASSWORD_RESET_COMPLETE_URL)
    return browser


# Shared steps
@then("I should see the username input")
def i_should_see_the_username_input(page):
    """I should see the username box."""
    page.assert_element("#id_username")


@when("clicks on recaptcha")
def clicks_on_recaptcha(page):
    page.switch_to_frame(
        "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']", timeout=10
    )
    page.click(
        "span.recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox"  # noqa: E501
    )
    page.switch_to_default_content()
    time.sleep(RECAPTCHA_SLEEP_INTERVAL)  # important! captcha needs time to execute


@when("clicks on submit button")
@then("clicks on submit button")
def clicks_on_submit_button(page, db):
    """clicks on submit button."""
    page.click('button[type="submit"]')


@then("User is able to see registration confirmation page")
def user_is_able_to_see_registration_confirmation_page(page, confirmation_page):
    assert page.get_current_url() == confirmation_page.get_current_url()


@then("required warning is visible")
def required_warning_is_visible(page):
    page.assert_element("input:required", by=By.CSS_SELECTOR)


@then("captcha warning is visible")
def captcha_warning_is_visible(page):
    page.assert_element("#error_1_id_captcha", by=By.CSS_SELECTOR)


@when("User enters valid username")
def user_enters_valid_username(page, user):
    page.type("#id_username", user.username)


@when("User enters valid email address")
def user_enters_valid_email_address(page, user_details):
    page.type("#id_email", user_details.email)


@then("an email is sent to the user's email address", target_fixture="confirm_link")
def an_email_is_sent_to_the_users_email_addresss(
    mailoutbox, user_details, request, page, settings
):
    m = mailoutbox[0]
    assert m.subject == "Confirm your email"
    assert m.from_email == settings.EMAIL_FROM_ADDRESS
    assert list(m.to) == [user_details.email]
    return m.extra_headers["LINK"]


@then("User is able to follow email link to successfully register")
def user_is_able_to_successfully_register(confirm_link, sb):
    sb.open(confirm_link)
    sb.assert_text("your account is confirmed", selector=".message", by=By.CSS_SELECTOR)
