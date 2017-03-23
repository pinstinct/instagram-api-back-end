from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = (
    'DeleteToken',
)


class DeleteToken(APIView):
    """
    Post 요청이 오면 reqest.user가 인증되어 있는 경우,
    request.auth의 Token을 삭제
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # user = request.user
        # token = Token.objects.get(user=user)
        # token.delete()
        request.auth.delete()
        return Response(status.HTTP_204_NO_CONTENT)
