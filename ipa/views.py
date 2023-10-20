import requests
from django.shortcuts import render
from .models import Visits, Parkings
from users.models import CustomUser, UserProfile
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ParkingSerializer, VisitsSerializer
from .utils import getParkings, find_free_parkings
from rest_framework.decorators import api_view

#This function serves the directions page to give back the 
@api_view(['GET'])
def directions(request):
    # latitude = request.data.get('latitude')
    # longitude = request.data.get('longitude')
    # results = getParkings(latitude, longitude)
    parkings = getParkings()
    if parkings is None:
        return Response(
            {'details': 'Could not find any parkings around, expand search', 'code': 400},
            status=status.HTTP_400_BAD_REQUEST
        )     
    return Response(
        {'details': parkings, 'code': 200},
        status=status.HTTP_200_OK
    )  

@api_view(['GET'])
def search_parking(request):
    context = []
    #values to be passed to getParkings Function
    # latitude = request.data.get('latitude')
    # longitude = request.data.get('longitude')
    # results = getParkings(latitude, longitude)
    parkings = getParkings()
    frees = find_free_parkings(parkings)
    
    #getting the location object to pass to the frontend
    for free in frees:
        free_parking = Parkings.objects.filter(location = free)
        serializer = ParkingSerializer(free_parking, many = True)
        context.append(serializer.data)
    
    return Response(
        {'details': context, 'code': 200},
        status=status.HTTP_200_OK
    )
    
# Here we get the visits of the user with the user id as a parameter in the URL.
@api_view(['GET'])
def visits(request, id):
    user = CustomUser.objects.get(id=id)
    
    if not Visits.objects.filter(user= user).exists():
        return Response(
            {'details': 'No visits yet', 'code': 400},
            status=status.HTTP_400_BAD_REQUEST
        )    
    
    visits = Visits.objects.filter(user= user)
    
    serializer = VisitsSerializer(visits, many=True)
    return Response(
        {'details': serializer.data, 'code': 200},
        status=status.HTTP_200_OK
    )  
    
