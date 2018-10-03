from rest_framework import generics, status
from .serializers import PartHistorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import PartHistory
from rest_framework.response import Response


class PartHistoryAPIView(generics.GenericAPIView):
    serializer_class = PartHistorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        qs = PartHistory.objects.filter(user=self.request.user)
        serializer = PartHistorySerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = PartHistorySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


