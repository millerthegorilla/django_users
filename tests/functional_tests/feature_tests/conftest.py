import pytest

from django.http import HttpRequest
from django.contrib.auth import (
		get_user_model,
		logout
	)
from django.conf import settings

User = get_user_model()

LOGIN_PAGE_ADDRESS = "/accounts/login/"

try:
	LANDING_PAGE_ADDRESS = settings.LOGIN_REDIRECT
except AttributeError:
	LANDING_PAGE_ADDRESS = "/accounts/profile/"

@pytest.fixture
def browser(sb, live_server):
	sb.visit(live_server)
	sb.domain = sb.get_domain_url(sb.get_current_url())
	yield sb

@pytest.fixture
def login_page(browser):
	browser.visit(browser.domain + LOGIN_PAGE_ADDRESS)
	yield browser

@pytest.fixture
def profile_page(browser):
	browser.visit(browser.domain + LANDING_PAGE_ADDRESS)
	yield browser

@pytest.fixture
def user(db):
	user = User.objects.create(username="bob", password="bob")
	yield user
