"""Buddies model."""
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from codebuddy.common.models import AbstractBase
from config import settings

from .managers import UserManager


class User(AbstractBaseUser):
    """Custom user model."""

    phone_number = PhoneNumberField(unique=True)
    display_name = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["display_name"]

    def __str__(self) -> str:
        """Human readable repr."""
        return str(self.phone_number)


class Buddy(AbstractBase):
    """Buddy (subscriber) information."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="user_profile_of",
    )

    def __str__(self) -> str:
        """Human readable representation."""
        return f"{self.user.display_name} ({self.user.phone_number})"
