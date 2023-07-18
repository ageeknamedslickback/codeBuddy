"""CodeBuddy gPRC server implementation."""
from concurrent import futures

import grpc

from codebuddy.buddies.models import Buddy
from codebuddy.grpc_service.generated import codebuddy_pb2_grpc


class CodeBuddyServicer(codebuddy_pb2_grpc.CodeBuddyServicer):
    """Provide methods that implement functionality of codeBuddy server."""

    def GetBuddy(self, request, context):
        """Implement get buddy service interface."""
        try:
            buddy = Buddy.objects.get(**request)
            return buddy

        except Buddy.DoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, "Buddy not found")


def serve():
    """Initialize gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    codebuddy_pb2_grpc.add_CodeBuddyServicer_to_server(
        CodeBuddyServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
