from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingViewset, VisitsViewset, FindParkingViewset

router = DefaultRouter()

router.register(r'admin-parkings', ParkingViewset, basename='parkings')
router.register(r'visits', VisitsViewset, basename='visits')
router.register(r'parkings', FindParkingViewset, basename='find-parking')

urlpatterns = [
    path('', include(router.urls))
]
