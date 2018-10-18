from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from userinfo.models import UserInfo
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout



class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class MyLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', False):
            userinfo = UserInfo.objects.filter(user=self.request.user).get()
            userinfo.push_id = None
            userinfo.save()

            response = self.logout(request)
        else:
            response = self.http_method_not_allowed(request, *args, **kwargs)

        return self.finalize_response(request, response, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        userinfo = UserInfo.objects.filter(user=self.request.user).get()
        userinfo.push_id=None
        userinfo.save()

        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        return Response({"detail": ("Successfully logged out.")},
                        status=status.HTTP_200_OK)
