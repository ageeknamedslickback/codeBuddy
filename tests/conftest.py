"""CodeBuddy test fixtures."""
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
