from django.shortcuts import render
from .models import Visits, Parkings
from users.models import CustomUser, UserProfile
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ParkingSerializer, VisitsSerializer

class ParkingViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Parkings.objects.all()
        
        serializer = ParkingSerializer(queryset, many = True)
        if not serializer.data:
            return Response(
                {'details': 'No parkings yet', 'code': 200},
                status= status.HTTP_200_OK
            )
         
        return Response(
            {'details': serializer.data, 'code': 200},
            status= status.HTTP_200_OK
        )   
        
    def create(self, request):
        serializer = ParkingSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'details': serializer.errors, 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
            
        serializer.save()
        return Response(
                {'details': 'Parking added successfully', 'code': 200},
                status= status.HTTP_200_OK
            )
        
    def retrieve(self, request, pk = None):
        try:
            parking = Parkings.objects.get(id = pk)
        except Parkings.DoesNotExist:
            return Response(
                {'details': 'Parking does nto exist', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
            
        serializer = ParkingSerializer(parking)
        return Response(
                {'details': serializer.data, 'code': 200},
                status= status.HTTP_200_OK
            )
        
    def update(self, request, pk = None):
        try:
            parking = Parkings.objects.get(id = pk)
        except Parkings.DoesNotExist:
            return Response(
                {'details': 'Parking does not exist', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ParkingSerializer(parking, data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'details': serializer.errors, 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        return Response(
                {'details': 'Parking updated', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        
    def destroy(self, request, pk = None):
        Parkings.objects.get(id = pk).delete()
        
        return Response(
            {'details': 'Delete successfull', 'code': 200},
            status= status.HTTP_200_OK
        )
        

#Visists Viewset
class VisitsViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Visits.objects.all()
        
        serializer = VisitsSerializer(queryset, many = True)
        if not serializer.data:
            return Response(
                {'details': 'No visits yet', 'code': 200},
                status= status.HTTP_200_OK
            )
         
        return Response(
            {'details': serializer.data, 'code': 200},
            status= status.HTTP_200_OK
        )   
        
    def create(self, request):
        user = request.data.get('user')
        parking = request.data.get('parking')
        
        if not CustomUser.objects.filter(id = user).exists():
            return Response(
                {'details': 'User does not exist', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        elif not Parkings.objects.filter(id = parking).exists():
            return Response(
                {'details': 'Parking does not exist', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
            
            
        serializer = VisitsSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'details': serializer.errors, 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
            
        serializer.save()
        return Response(
                {'details': 'Visit added successfully', 'code': 200},
                status= status.HTTP_200_OK
            )
        
    def retrieve(self, request, pk = None):
        try:
            visit = Visits.objects.get(id = pk)
        except Visits.DoesNotExist:
            return Response(
                {'details': 'Parking does nto exist', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
            
        serializer = VisitsSerializer(visit)
        return Response(
                {'details': serializer.data, 'code': 200},
                status= status.HTTP_200_OK
            )
        
    def update(self, request, pk = None):
        pass
    
    def destroy(self, request, pk = None):
        pass
        
        