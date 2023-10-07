from django.urls import path, include
from .views import UserViewset, UserProfileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewset, basename='users'),
router.register(r'profile', UserProfileViewset, basename='profile')

urlpatterns = [
    path('', include(router.urls))
]
