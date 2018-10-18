from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views
from userinfo.task import send_fcm_test
from .views import MyLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/logout/', MyLogoutView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/kakao/', views.KakaoLogin.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('django.contrib.auth.urls')),
    #path('accounts/', include('allauth.urls')),

    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),

    path('userinfo/', include('userinfo.urls')),
    path('video/', include('video.urls')),
    path('recommend/', include('recommend_list.urls')),
    path('videolist/', include('video_list.urls')),
    path('version/', include('version.urls')),

    # test
    path('test/', send_fcm_test),
]
