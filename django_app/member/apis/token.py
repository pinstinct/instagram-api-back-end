from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from rest_auth.views import LogoutView as RestLogoutView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = (
    'DeleteToken',
    'LogoutView',
)


class LogoutView(RestLogoutView):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        django_logout(request)
        return Response({"detail": _("Successfully logged out.")},
                        status=status.HTTP_200_OK)


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
