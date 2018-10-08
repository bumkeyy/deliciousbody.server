from rest_framework.serializers import ModelSerializer
from .models import UserInfo


class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = UserInfo
        exclude = ('user', 'prev_video_id', 'next_video_id',
                   'prev_hour', 'next_hour', 'weekdays_push_list', 'weekend_push_list',)