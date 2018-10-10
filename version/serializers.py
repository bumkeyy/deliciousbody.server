from rest_framework.serializers import ModelSerializer
from .models import Version


class VersionSerializer(ModelSerializer):

    class Meta:
        model = Version
        fields = '__all__'