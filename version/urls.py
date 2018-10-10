from django.urls import path
from .views import LatestVersionView

urlpatterns=[
    path('', LatestVersionView.as_view()),
]

