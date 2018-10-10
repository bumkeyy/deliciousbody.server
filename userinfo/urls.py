from django.urls import path
from .views import UserInfoAPIView, PushAPIView
from .task import push_task

urlpatterns = [
    path('', UserInfoAPIView.as_view()),
    path('push/', PushAPIView.as_view()),
    path('task', push_task),
    path('task/', push_task),
]
