"""Buddies custom manager."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Custom user manager."""

    def create_user(self, phone_number, display_name, password=None):
        """Create and save a User.

        with the given phone number, display_name and password.
        """
        user = self.model(phone_number=phone_number, display_name=display_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
