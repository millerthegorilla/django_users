from pytest_bdd import given, scenarios

scenarios("../resend_confirmation.feature")


@given("User is on resend confirmation page", target_fixture="page")
def user_is_on_resend_confirmation_page(resend_confirmation_page):
    """User is on resend_confirmation page"""
    return resend_confirmation_page


# @when("User enters valid username") - shared in conftest.py
