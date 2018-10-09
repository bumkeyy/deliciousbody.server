from rest_framework.serializers import ModelSerializer
from .models import RecommendList
from video.models import Video
from video_list.models import VideoList
from video.serializers import VideoSerializer
from rest_framework import serializers

class RecommendListSerializer(ModelSerializer):
    video_list = serializers.SerializerMethodField()

    class Meta:
        model = RecommendList
        fields = ('list_id', 'list_name', 'list_count', 'time', 'list_image', 'video_list')

    def get_video_list(self, obj):
        if not obj.videolist:
            return None
        list_id = obj.videolist.list_id
        vl = VideoList.objects.filter(list_id=list_id).get()
        all_video = Video.objects.all()
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

        return VideoSerializer(qs, many=True).data

