from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingViewset, VisitsViewset

router = DefaultRouter()

router.register(r'parkings', ParkingViewset, basename='parkings')
router.register(r'visits', VisitsViewset, basename='visits')

urlpatterns = [
    path('', include(router.urls))
]
