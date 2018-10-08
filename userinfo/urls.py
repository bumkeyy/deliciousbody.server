from django.urls import path
from .views import UserInfoAPIView, PushAPIView

urlpatterns = [
    path('', UserInfoAPIView.as_view()),
    path('push/', PushAPIView.as_view()),
]
