"""Login page feature tests."""
import pytest
from django.contrib.auth import get_user_model
from pytest_bdd import given, parsers, scenarios, then, when

EXTRA_TYPES = {
    "String": str,
}

scenarios("../login.feature")


# SHARED STEPS - could go in conftest.py - but is appropriate for this file.s
@given("User is on login page", target_fixture="page")
def user_is_on_login_page(login_page):
    """User is on login page."""
    return login_page


# @then("I should see the username input") shared in conftest.py


@then("I should see the password input")
def i_should_see_the_password(page):
    """I should see the password."""
    page.assert_element("#id_password")


@then("I should see the registration link")
def i_should_see_the_register_link(page):
    """I should see the register link."""
    page.assert_element(page.links["registration"])


@then("I should see the reset password link")
def i_should_see_the_reset_password_link(page):
    """I should see the reset password link."""
    page.assert_element(page.links["reset_password"])


@then("I should see a submit button")
def i_should_see_a_submit_button(page):
    """I should see the username box."""
    page.assert_element('button[type="submit"]')


@when("User fills valid username and password")
def user_fills_valid_username_and_password(page, user_details):
    """User fills valid username and password."""
    page.type("#id_username", user_details.username)
    page.type("#id_password", user_details.password)


# @when("clicks on submit button") - shared in conftest.py


@then("User is able to login and view landing page")
def user_is_able_to_login_and_view_landing_page(page, landing_page):
    """User is able to login and view landing page."""
    assert page.get_current_url() == landing_page.get_current_url()


@when(parsers.cfparse('User clicks "{link:String}" link', extra_types=EXTRA_TYPES))
def user_clicks_link(link, page):
    """User is able to view and click [ reset password | registration ] link"""
    page.click(page.links[link])


@then(
    parsers.cfparse(
        'User is taken to "{page_url:String}" page', extra_types=EXTRA_TYPES
    )
)
def user_is_taken_to_page(page, page_url):
    """User is able to visit [ reset password | registration ] page"""
    assert page.get_current_url() == (page.domain + page.pages[page_url])
