from .serializers import VideoSerializer
from .models import Video
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsSuperUserUpdateOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회을 허용
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
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
    """
    # Return a Video Info
    ---
    영상 정보를 반환
    video_name (string) : 영상 이름
    level (integer) : 영상 활동 수준 (default = 1, 0 < 2)
    part1 (boolean) : 부위 1 (default = true)
    part2 (boolean) : 부위 2 (default = false)
    part3 (boolean) : 부위 3 (default = false)
    part4 (boolean) : 부위 4 (default = false)
    part5 (boolean) : 부위 5 (default = false)
    part6 (boolean) : 부위 6 (default = false)
    part7 (boolean) : 부위 7 (default = false)
    part8 (boolean) : 부위 8 (default = false)
    time (integer) : 영상 시간
    description (string) : 영상 설명 (maxsize = 300)
    video_url (string) : 영상 url
    video_file (file) : 영상 file
    create_at (DateTime) : 영상 정보 생성 시간
    updated_at (DateTime) : 영상 정보 갱신 시간
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]




