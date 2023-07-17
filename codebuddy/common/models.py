"""Common app models."""
import uuid

from django.db import models


class AbstractBase(models.Model):
    """Abstract base model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.UUIDField(null=True, blank=True)

    class Meta:
        """Abstract base meta options."""

        abstract = True
        ordering = ("-updated", "-created")
