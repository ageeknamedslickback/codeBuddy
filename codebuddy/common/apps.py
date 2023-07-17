"""Common app configuration."""
from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Common config class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "codebuddy.common"
