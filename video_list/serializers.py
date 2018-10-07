from rest_framework.serializers import ModelSerializer
from .models import VideoList
from video.serializers import VideoSerializer


class VideoListSerializer(ModelSerializer):
    video1 = VideoSerializer()
    video2 = VideoSerializer()
    video3 = VideoSerializer()
    video4 = VideoSerializer()
    video5 = VideoSerializer()

    class Meta:
        model = VideoList
        fields = ('list_id', 'list_name','video1', 'video2', 'video3', 'video4', 'video5')
