from .serializers import RecommendListSerializer
from .models import RecommendList
from userinfo.models import UserInfo
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsSuperUserUpdateOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회을 허용
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        elif request.user.is_superuser and request.user.is_staff:
            return True
        return False

    # superuser에게는 입력, 삭제 권한만 부여하고
    def has_object_permission(self, request, view, obj):
        # 조회 요청(GET, HEAD, OPTIONS) 에 대해서는 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # 삭제 요청의 경우, superuser에게만 허용
        if (request.method != SAFE_METHODS) :
            return request.user.is_superuser  # request.user.is_staff

        return False



class RecommendListView(generics.GenericAPIView):
    serializer_class = RecommendListSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request):
        qs = RecommendList.objects.all()
        serializer = RecommendListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecommendListDetailView(generics.GenericAPIView):
    serializer_class = RecommendListSerializer
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request, pk):
        qs = RecommendList.objects.filter(list_id=pk)
        serializer = RecommendListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecommendToUserView(generics.GenericAPIView):
    serializer_class = RecommendListSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsSuperUserUpdateOrReadonly]

    def get(self, request):
        interest = UserInfo.objects.filter(user=self.request.user).values_list('interested_part', flat=True).get(pk=1)
        interest_list = interest.split(';')
        qs_list = RecommendList.objects.all()
        qs = RecommendList.objects.none()

        # 관심있는 부위를 포함하는 추천 리스트가 있다면 추가
        if '1' in interest_list:
            qs = qs_list.filter(part1 = True)
        if '2' in interest_list:
            qs = qs | qs_list.filter(part2 = True)
        if '3' in interest_list:
            qs = qs | qs_list.filter(part3 = True)
        if '4' in interest_list:
            qs = qs | qs_list.filter(part4 = True)
        if '5' in interest_list:
            qs = qs | qs_list.filter(part5 = True)
        if '6' in interest_list:
            qs = qs | qs_list.filter(part6 = True)
        if '7' in interest_list:
            qs = qs | qs_list.filter(part7 = True)
        if '8' in interest_list:
            qs = qs | qs_list.filter(part8 = True)


        serializer = RecommendListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




