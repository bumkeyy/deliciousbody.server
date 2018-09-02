from django.urls import path
from .views import UserInfoAPIView

urlpatterns = [
    path('', UserInfoAPIView.as_view()),
]
