"""Buddies app test cases."""
from codebuddy.buddies.models import Buddy, User


def test_user_creation(user):
    """Verify creation of a user."""
    assert User.objects.count() == 1
    assert str(user) == "+254711223344"


def test_buddy_creation(buddy, user):
    """Verify creation of a buddy."""
    assert Buddy.objects.count() == 1
    assert str(buddy) == "Vigilant Otter (+254711223344)"
    assert buddy.user == user
    assert buddy.active
    assert hasattr(buddy, "id")
