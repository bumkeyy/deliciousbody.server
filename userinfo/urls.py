from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserInfoAPIView.as_view()),
]
