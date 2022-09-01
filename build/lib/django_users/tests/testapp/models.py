from django.contrib import auth

from django_users.tests.conftest import UserDetails

User = auth.get_user_model()


class DjangoUser:
    def __init__(self):
        self.user = User.objects.create(
            username=UserDetails.username,
            email=UserDetails.password,
            password=UserDetails.password,
        )
