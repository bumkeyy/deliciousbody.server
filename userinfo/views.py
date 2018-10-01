from rest_framework import generics, status
from .serializers import UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import UserInfo
from rest_framework.response import Response


class UserInfoAPIView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        qs = UserInfo.objects.filter(user=self.request.user)
        serializer = UserInfoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = UserInfoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):

        info = UserInfo.objects.filter(user=self.request.user).first()
        serializer = UserInfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
