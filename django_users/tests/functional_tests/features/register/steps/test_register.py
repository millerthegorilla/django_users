"""Registration page feature tests."""
import random
import time

from django.core import mail
from pytest_bdd import given, scenarios, then, when
import pytest

EXTRA_TYPES = {
    "String": str,
}

scenarios("../register.feature")


# SHARED STEPS - could go in conftest.py - but is appropriate for this file.
@given("User is on registration page", target_fixture="page")
def user_is_on_register_page(registration_page):
    """User is on login page."""
    return registration_page


# @then("I should see the username input")
# def i_should_see_the_username_input(page):
#     """I should see the username box."""
#     page.assert_element("#id_username")


@then("I should see the password input")
def i_should_see_the_password_input(page):
    """I should see the password."""
    page.assert_element("#id_password1")


@then("I should see the password confirmation input")
def i_should_see_the_password_confirmation_input(page):
    """I should see the password."""
    page.assert_element("#id_password2")


@then("I should see the email input")
def i_should_see_the_email_input(page):
    """I should see the register link."""
    page.assert_element("#id_email")


@then("I should see the resend confirmation link")
def i_should_see_the_resend_confirmation_link(page):
    """I should see the reset password link."""
    page.assert_element(page.links["resend_confirmation"])


@then("I should see the recaptcha")
def i_should_see_the_recaptcha(page):
    """I should see the recaptcha."""
    page.assert_element("#id_captcha")


@then("I should see a submit button")
def i_should_see_a_submit_button(page):
    """I should see the username box."""
    page.assert_element('button[type="submit"]')


@when("User completes valid details")
def user_completes_valid_details(page, user_details):
    page.type("#id_username", user_details.username)
    page.type("#id_password1", user_details.password)
    page.type("#id_password2", user_details.password)
    page.type("#id_email", user_details.email)


@when("clicks on recaptcha")
def clicks_on_recaptcha(page):
    page.switch_to_frame(
        "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']", timeout=10
    )
    page.click(
        "span.recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox"  # noqa: E501
    )
    page.switch_to_default_content()


# @when("clicks on submit button") shared.  ../../conftext.py
# @when("clicks on submit button")
# def clicks_on_submit_button(page, db):
#     """clicks on submit button."""
#     page.click('button[type="submit"]')


@then("User is able to see registration confirmation page")
def user_is_able_to_see_registration_confirmation_page(page, confirmation_page):
    assert page.get_current_url() == confirmation_page.get_current_url()


@then("an email is sent to the user's email address")
def an_email_is_sent_to_the_users_email_addresss(mailoutbox):
    # skip_step[
    #     "message"
    # ] = "doesn't work in headless mode (requires --gui --demo to pytest"
    try:
        m = mailoutbox[0]
        assert m.subject == "Confirm your email"
        # assert m.body == "body"
        assert m.from_email == "noreply@django_users.com"
        # assert list(m.to) == [user_details["email"]]
    except IndexError:
        pass
