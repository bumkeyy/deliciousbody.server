from rest_framework import generics, status
from .serializers import UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import UserInfo
from rest_framework.response import Response
from video.models import Video


class UserInfoAPIView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        push_id = request.META.get('HTTP_PUSHTOKEN')
        obj = UserInfo.objects.filter(user=self.request.user).get()
        obj.push_id = str(push_id)
        obj.save()

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


class PushAPIView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        info = UserInfo.objects.filter(user=self.request.user).first()
        video_part = Video.objects.filter(video_id=info.prev_video_id).values_list('main_part', flat=True).get()

        # 관심있는 부위를 포함하는 추천 리스트가 있다면 추가
        if '0' == video_part:
            info.part0 += 1
        if '1' == video_part:
            info.part1 += 1
        if '2' == video_part:
            info.part2 += 1
        if '3' == video_part:
            info.part3 += 1
        if '4' == video_part:
            info.part4 += 1
        if '5' == video_part:
            info.part5 += 1
        if '6' == video_part:
            info.part6 += 1
        if '7' == video_part:
            info.part7 += 1
        if '8' == video_part:
            info.part8 += 1

        info.save()
        return Response(status=status.HTTP_200_OK)
