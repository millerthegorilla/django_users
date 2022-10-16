from django.contrib.auth import get_user_model

User = get_user_model()


def test_user_model_signal_is_triggered(user_details, db):
    user = User.objects.create(username=user_details.username, email=user_details.email)
    assert user.is_active == False


def test_user_is_not_active_when_created(db, user):
    assert user.is_active == False
