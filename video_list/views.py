from .serializers import VideoListSerializer
from .models import VideoList
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from video.models import Video
from video.serializers import VideoSerializer
from django.core.cache import cache

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
    serializer_class = VideoListSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request):
        qs = VideoList.objects.all()
        serializer = VideoListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VideoDetailView(generics.GenericAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request, pk):
        cache_name_list = ['vl']
        cache_name_list.append(str(pk))
        cache_name = ''.join(cache_name_list)
        data = cache.get(cache_name)

        if data is None:
            vl = VideoList.objects.filter(list_id=pk).get()

            all_video = cache.get('all_video')
            if all_video is None:
                all_video = Video.objects.all()
                cache.set('all_video', all_video)
            qs = Video.objects.none()

            for i in range(1, vl.list_count + 1):
                if i == 1:
                    qs = qs | all_video.filter(video_id=vl.video1.video_id)
                if i == 2:
                    qs = qs | all_video.filter(video_id=vl.video2.video_id)
                if i == 3:
                    qs = qs | all_video.filter(video_id=vl.video3.video_id)
                if i == 4:
                    qs = qs | all_video.filter(video_id=vl.video4.video_id)
                if i == 5:
                    qs = qs | all_video.filter(video_id=vl.video5.video_id)
            data = VideoSerializer(qs, many=True).data
            cache.set(cache_name, data)

        return Response(data, status=status.HTTP_200_OK)


