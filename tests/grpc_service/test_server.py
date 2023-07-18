"""Test gRPC service definition."""
from codebuddy.grpc_service.codebuddy_server import CodeBuddyServicer
from codebuddy.grpc_service.generated.codebuddy_pb2 import (
    GetBuddyRequest,
)


def test_code_buddy_service(buddy):
    """Verify invoking bode buddy grpc service."""
    service = CodeBuddyServicer()
    request = GetBuddyRequest(phone_number=buddy.phone_number)
    response = service.GetBuddy(request)

    assert response
