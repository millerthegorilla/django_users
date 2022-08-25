import pytest
from django.shortcuts import reverse
from django.test import TestCase


class TestLogin(TestCase):
    def test_uses_login_template(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")


class TestRegistration(TestCase):
    def test_uses_registration_template(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "django_users/register.html")
