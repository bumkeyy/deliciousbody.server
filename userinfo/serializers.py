from rest_framework.serializers import ModelSerializer
from .models import UserInfo


class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['name', 'age', 'is_man', 'activity_level', 'interested_part',
                  'weekdays_start', 'weekdays_end', 'weekend_start', 'weekend_end',
                  'avatar', 'comment', 'favorite_list', 'is_push']