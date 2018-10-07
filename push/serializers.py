from rest_framework.serializers import ModelSerializer
from .models import Push


class PushSerializer(ModelSerializer):

    class Meta:
        model = Push
        exclude = ('user',)