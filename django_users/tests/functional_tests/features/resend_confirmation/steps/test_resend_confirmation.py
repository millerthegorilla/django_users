from pytest_bdd import given, scenarios

scenarios("../resend_confirmation.feature")


@given("User is on resend confirmation page", target_fixture="page")
def user_is_on_resend_confirmation_page(resend_confirmation_page):
    """User is on resend_confirmation page"""
    return resend_confirmation_page


# @when("User enters valid username") - shared in conftest.py


# @when("clicks on recaptcha") - shared in conftest.py


# @when("clicks on submit button") - shared in conftest.py


# @then("an email is sent to the user's email address", target_fixture="confirm_link") - shared in conftest.py  # noqa: E501


# @then("User is able to follow email link to successfully register") -shared in conftest.py  # noqa: E501


# @then("User is able to see registration confirmation page") - shared in conftest.py  # noqa: E501, W292
