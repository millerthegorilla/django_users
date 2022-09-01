"""Password reset page feature tests."""

import re

from django.core import mail
from pytest_bdd import given, scenarios, then

scenarios("../password_reset.feature")


@given("User is on reset password page", target_fixture="page")
def user_is_on_reset_password_page(reset_password_page, active_user):
    """User is on reset password page"""
    return reset_password_page


@then("User is able to see password done page")
def password_reset_done_is_visible(page, reset_password_done_page):
    assert page.get_current_url() == reset_password_done_page.get_current_url()


@then("User is sent password reset email", target_fixture="reset_link")
def user_is_sent_password_reset_email(
    mailoutbox, user_details, request, page, settings
):
    m = mailoutbox[0]
    assert "Password reset" in m.subject
    link = re.search(r"http.*", m.body).group()
    assert page.domain in link
    assert m.from_email == settings.EMAIL_FROM_ADDRESS
    assert list(m.to) == [user_details.email]
    return link


@then("User can follow link")
def user_can_follow_link(page, reset_link):
    page.open(reset_link)


@then("User can view password reset confirm page")
def user_can_view_password_reset_page(page):
    assert "Password Reset Confirmation" in page.get_title()


@then("User can enter password twice")
def user_can_enter_password_twice(page, user_details):
    page.type("#id_new_password1", user_details.password)
    page.type("#id_new_password2", user_details.password)


# @then("clicks on submit button") - shared in conftest.py


@then("User can see password reset complete page")
def user_can_see_password_reset_complete_page(page, reset_password_complete_page):
    assert page.get_current_url() == reset_password_complete_page.get_current_url()
