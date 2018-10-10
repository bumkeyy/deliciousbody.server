from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import VersionSerializer
from .models import Version
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class LatestVersionView(generics.GenericAPIView):
    serializer_class = VersionSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        qs = Version.objects.latest('created_at')
        serializer = VersionSerializer(qs)
        return Response(serializer.data, status=status.HTTP_200_OK)




