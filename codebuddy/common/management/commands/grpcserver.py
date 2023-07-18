"""Run the gRPC server."""
from typing import Any

from django.core.management.base import BaseCommand

from codebuddy.grpc_service.codebuddy_server import serve


class Command(BaseCommand):
    """Initialize and run the gRPC server."""

    def handle(self, *args: Any, **options: Any) -> str | None:
        """Handle the actual management command."""
        self.stdout.write(
            self.style.SUCCESS("Running gRPC codeBuddy service on port 50051")
        )
        serve()
