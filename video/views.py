from .serializers import VideoSerializer
from .models import Video
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsSuperUserUpdateOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회을 허용
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        elif request.user.is_superuser and request.user.is_staff:
            return True
        return False

    # superuser에게는 입력, 삭제 권한만 부여하고
    def has_object_permission(self, request, view, obj):
        # 조회 요청(GET, HEAD, OPTIONS) 에 대해서는 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # 삭제 요청의 경우, superuser에게만 허용
        if (request.method != SAFE_METHODS) :
            return request.user.is_superuser  # request.user.is_staff

        return False


class VideoAPIViewSet(ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]
    #permission_classes = [IsAuthenticated]




