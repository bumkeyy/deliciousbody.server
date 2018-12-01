from django.urls import path
from .views import UserInfoAPIView, PushAPIView, TypeAPIView
from .task import push_task

urlpatterns = [
    path('', UserInfoAPIView.as_view()),
    path('push/', PushAPIView.as_view()),

    path('type/<int:pk>/', TypeAPIView.as_view()),

    path('task/', push_task),
]
