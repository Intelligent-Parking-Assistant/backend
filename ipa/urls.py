from django.urls import path, include
from . import views

urlpatterns = [
    path('directions/', views.directions, name= 'directions'),
    path('search/', views.search_parking, name= 'search'),
    path('visits/<id>/', views.visits, name= 'visits')
]
