from django.urls import path
from .views import VideoDetailView, VideoListView, VideoLikeView

urlpatterns=[
    path('', VideoListView.as_view()),
    path('<int:pk>/', VideoDetailView.as_view()),
    path('like/', VideoLikeView.as_view()),
]

