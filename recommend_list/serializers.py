from rest_framework.serializers import ModelSerializer
from .models import RecommendList


class RecommendListSerializer(ModelSerializer):

    class Meta:
        model = RecommendList
        fields = '__all__'