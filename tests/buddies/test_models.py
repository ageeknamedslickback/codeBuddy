"""Buddies app test cases."""
import pytest
from model_bakery import baker

from codebuddy.buddies.models import Buddy, User

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    """Create test user."""
    return baker.make(
        User,
        phone_number="+254711223344",
        display_name="Vigilant Otter",
    )


@pytest.fixture
def buddy(user):
    """Create test buddy."""
    return baker.make(Buddy, user=user)


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
