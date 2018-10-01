from rest_framework.serializers import ModelSerializer
from .models import PartHistory


class PartHistorySerializer(ModelSerializer):

    class Meta:
        model = PartHistory
        exclude = ('user',)