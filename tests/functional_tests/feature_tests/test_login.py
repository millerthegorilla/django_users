"""Login page feature tests."""

import pytest
from functools import partial

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from .conftest import LOGIN_PAGE_ADDRESS

scenario = partial(scenario, "../features/login.feature")

## SHARED STEPS - could go in conftest.py - but this is appropriate for this file.
@given('User is on login page')
def user_is_on_login_page(login_page):
    """User is on login page."""
    assert(login_page.get_current_url() == LOGIN_PAGE_ADDRESS)

## SCENARIO 1 of 2
@scenario('Login to Application')
def test_login_to_application(sb):
    """Login to Application."""

@when('User fills valid username and password')
def user_fills_valid_username_and_password(login_page, user):
    """User fills valid username and password."""
    login_page.type("#id_username", user.username)
    login_page.type("#id_password", user.password)

@when('clicks on submit button')
def clicks_on_submit_button(login_page):
    """clicks on submit button."""
    login_page.click('button[type="submit"]')

@then('User is able to login and view landing page')
def user_is_able_to_login_and_view_landing_page(login_page, profile_page):
    """User is able to login and view landing page."""
    assert(login_page.get_current_url() == profile_page.get_current_url())

## SCENARIO 2 of 2
@scenario('Visiting the login page')
def test_visiting_the_login_page():
    """Visiting the login page."""

@then('I should see the password box')
def i_should_see_the_password(login_page):
    """I should see the password."""
    login_page.assert_element('#id_password')

@then('I should see the register link')
def i_should_see_the_register_link(login_page):
    """I should see the register link."""
    login_page.assert_element('a[href="/accounts/register/"]')

@then('I should see the reset password link')
def i_should_see_the_reset_password_link(login_page):
    """I should see the reset password link."""
    login_page.assert_element('a[href="/accounts/password_reset/"]')

@then('I should see the username box')
def i_should_see_the_username_box(login_page):
    """I should see the username box."""
    login_page.assert_element('#id_username')

@then('I should see a submit button')
def i_should_see_a_submit_button(login_page):
    """I should see the username box."""
    login_page.assert_element('button[type="submit"]')