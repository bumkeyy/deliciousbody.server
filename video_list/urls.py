from django.urls import path
from .views import VideoDetailView, VideoListView

urlpatterns=[
    path('', VideoListView.as_view()),
    path('<int:pk>/', VideoDetailView.as_view()),
]
