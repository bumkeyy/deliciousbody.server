from .serializers import VideoSerializer
from .models import Video
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from userinfo.models import UserInfo

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


class VideoListView(generics.GenericAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request):
        qs = Video.objects.all()
        serializer = VideoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VideoDetailView(generics.GenericAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request, pk):
        obj = Video.objects.filter(video_id=pk).get()
        serializer = VideoSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VideoLikeView(generics.GenericAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request):
        favorite = UserInfo.objects.filter(user=self.request.user).values_list('favorite_list', flat=True).get()
        flist = favorite.split(';')
        v_list = Video.objects.all()
        qs = Video.objects.none()

        for i in flist:
            vid = int(i)
            qs = qs | v_list.filter(video_id = vid)

        serializer = VideoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


