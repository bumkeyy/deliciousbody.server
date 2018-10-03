from django.urls import path
from .views import RecommendListDetailView, RecommendListView

urlpatterns=[
    path('', RecommendListView.as_view()),
    path('<int:pk>/', RecommendListDetailView.as_view()),
]

