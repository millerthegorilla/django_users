import pytest

from django.http import HttpRequest
from django.contrib.auth import (
		get_user_model,
		logout
	)
from django.conf import settings

User = get_user_model()

LOGIN_PAGE_ADDRESS = "http://127.0.0.1:8000/accounts/login/"

try:
	LANDING_PAGE_ADDRESS = settings.LOGIN_REDIRECT
except AttributeError:
	LANDING_PAGE_ADDRESS = "http://127.0.0.1:8000/accounts/profile/"

@pytest.fixture
def login_page(sb):
	sb.visit(LOGIN_PAGE_ADDRESS)
	yield sb

@pytest.fixture
def profile_page(sb):
	sb.visit(LANDING_PAGE_ADDRESS)
	yield sb

@pytest.fixture
def user(db):
	user = User.objects.create(username="bob", password="bob")
	yield user
