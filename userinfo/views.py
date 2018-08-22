from rest_framework import generics, status
from .serializers import UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UserInfo
from rest_framework.response import Response


class UserInfoAPIView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        # Return a User Info
        ---
        유저의 유저 정보를 반환
u
        name (string) : 유저의 닉네임
        age (integer) : 유저의 나이
        is_man (boolean) : 남자인지 여자인지 (True 일때 남자)
        activity_level (integer) : 활동 수준 (0, 1, 2, default = 1)
        intersted_part (array): 관심 부위 (0 ~ 7, maxsize = 8)
        weekdays_start (integer) : 주중 알림 시작 시간 (default = 8)
        weekdays_end (integer) : 주중 알림 종료 시간 (default = 22)
        weekdend_start (integer) : 주말 알림 시작 시간 (default = 8)
        weekdend_end (integer) : 주말 알림 종료 시간 (default = 22)
        comment (string) : 동기 부여 멘트 (maxsize = 12)
        avatar (image) : 아바타 사진 (unique = False)
        favorite_list (array) : 하트 누른 부위
        create_at (DateTime) : 유저 정보 생성 시간
        updated_at (DateTime) : 유저 정보 갱신 시간
        is_push (boolean) : 알림 활성화 버튼 (default = True)

        """
        qs = UserInfo.objects.filter(user=self.request.user)
        serializer = UserInfoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        # Create User Info
        ---
        유저의 유저 정보를 생성

        name (string) : 유저의 닉네임
        age (integer) : 유저의 나이
        is_man (boolean) : 남자인지 여자인지 (True 일때 남자)
        activity_level (integer) : 활동 수준 (0, 1, 2, default = 1)
        intersted_part (array): 관심 부위 (0 ~ 7, maxsize = 8)
        weekdays_start (integer) : 주중 알림 시작 시간 (default = 8)
        weekdays_end (integer) : 주중 알림 종료 시간 (default = 22)
        weekdend_start (integer) : 주말 알림 시작 시간 (default = 8)
        weekdend_end (integer) : 주말 알림 종료 시간 (default = 22)
        comment (string) : 동기 부여 멘트 (maxsize = 12)
        avatar (image) : 아바타 사진 (unique = False)
        favorite_list (array) : 하트 누른 부위
        is_push (boolean) : 알림 활성화 버튼 (default = True)

        성공시 201, 실패시 401
        """
        serializer = UserInfoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        """
        # Create User Info
        ---
        유저의 유저 정보를 생성

        name (string) : 유저의 닉네임
        age (integer) : 유저의 나이
        is_man (boolean) : 남자인지 여자인지 (True 일때 남자)
        activity_level (integer) : 활동 수준 (0, 1, 2, default = 1)
        intersted_part (array): 관심 부위 (0 ~ 7, maxsize = 8)
        weekdays_start (integer) : 주중 알림 시작 시간 (default = 8)
        weekdays_end (integer) : 주중 알림 종료 시간 (default = 22)
        weekdend_start (integer) : 주말 알림 시작 시간 (default = 8)
        weekdend_end (integer) : 주말 알림 종료 시간 (default = 22)
        comment (string) : 동기 부여 멘트 (maxsize = 12)
        avatar (image) : 아바타 사진 (unique = False)
        favorite_list (array) : 하트 누른 부위
        is_push (boolean) : 알림 활성화 버튼 (default = True)

        성공시 200, 실패시 400
        """
        info = UserInfo.objects.filter(user=self.request.user).first()
        serializer = UserInfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

