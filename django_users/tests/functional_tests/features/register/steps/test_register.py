"""Registration page feature tests."""
from django.contrib.auth import get_user_model
from pytest_bdd import given, scenarios, then, when
from selenium.webdriver.common.by import By

EXTRA_TYPES = {
    "String": str,
}

scenarios("../register.feature")
User = get_user_model()

# SHARED STEPS - could go in conftest.py - but is appropriate for this file.
@given("User is on registration page", target_fixture="page")
def user_is_on_register_page(registration_page):
    """User is on login page."""
    return registration_page


# @then("I should see the username input") - shared in conftest.py


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


# @when("clicks on recaptcha") - shared in conftest.py


# @when("clicks on submit button") - shared in conftest.py


# @then("an email is sent to the user's email address", target_fixture="confirm_link") - shared in conftest.py


# @then("User is able to follow email link to successfully register") -shared in conftest.py


# @then("User is able to see registration confirmation page") - shared in conftest.py


@when("User clicks resend confirmation link")
def user_clicks_link(page):
    """User is able to view and click [ reset password | registration ] link"""
    page.click(page.links["resend_confirmation"])


@then("User is taken to resend confirmation page")
def user_is_taken_to_page(page, resend_confirmation_page):
    """User is able to visit [ reset password | registration ] page"""
    assert page.get_current_url() == resend_confirmation_page.get_current_url()


# @when("User enters valid email address") - shared in conftest.py


@when("User enters valid password1")
def user_enters_valid_password1(page, user_details):
    page.type("#id_password1", user_details.password)


@when("User enters valid password2")
def user_enters_valid_password2(page, user_details):
    page.type("#id_password2", user_details.password)


@when("User enters incorrect email address")
def user_enters_incorrect_email_address(page):
    page.type("#id_email", "bob@bob")


@then("invalid email message is visible")
def invalid_email_message_is_visible(page):
    page.assert_element("#error_1_id_email", by=By.CSS_SELECTOR)


@given("User opens invalid link", target_fixture="page")
def user_opens_invalid_link(browser, db):
    browser.open(
        browser.domain
        + (
            "/email"
            "/email"
            "/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
            ".eyJlbWFpbCI6IkphbWVzX0RhdmlzQGFuZHJl"
            "d3MuaW5mbyIsImV4cCI6MTY2MjQ3MDA4MC45N"
            "jU2NDIsImtpbmQiOiJNQUlMIn0.YgGUFEbi_Q"
            "mgIbLyRqy5icqxkzn8EelQiy9OXYegOws"
        )
    )
    return browser


@then("error is shown in template")
def error_is_shown_in_template(page):
    assert "You tried to register with an invalid token!" in page.get_page_source()
