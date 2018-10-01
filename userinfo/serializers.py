from rest_framework.serializers import ModelSerializer
from .models import UserInfo


class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = UserInfo
        exclude = ('user',)