from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoAPIViewSet


router = DefaultRouter()
router.register('', VideoAPIViewSet)

urlpatterns=[
    path('', include(router.urls)),
]

