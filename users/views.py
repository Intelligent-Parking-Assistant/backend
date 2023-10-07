from django.shortcuts import render
from .models import CustomUser, UserProfile
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer

class UserViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many= True)
        
        if not serializer.data:
            return Response(
                {'details': serializer.errors, 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'details': serializer.data, 'code': 200},
            status=status.HTTP_200_OK
        )
        
    def create(self, request):
        email = request.data.get('email')
        
        if CustomUser.objects.filter(email = email).exists():
            return Response(
                {'details': 'User already exists', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'details': serializer.errors, 'code': 400},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        return Response(
            {'details': 'User added', 'code': 200},
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk= None):
        try:
            # check if the user exists.
            user = CustomUser.objects.get(id = pk)
        except CustomUser.DoesNotExist:
            return Response(
                    {'detail': 'User Does not exist', 'code': 400},
                        status = status.HTTP_400_BAD_REQUEST
                )
        
        serializer = UserSerializer(user)
        return Response(
                {'data': serializer.data, 'code': 200},
                status = status.HTTP_200_OK
                )
    def update(self, request, pk = None):
        try:
            user = CustomUser.objects.get(id = pk)
        except CustomUser.DoesNotExist:
            return Response(
                {'details': 'Could not find User', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
        #Allow change of email but the email should not be changed to an already existing email.  
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'details': 'Updated succefully', 'code':200},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'details': serializer.errors, 'code':400},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, pk=id):
        CustomUser.objects.get(pk=pk).delete()
        return Response(
            {'details': 'Delete Succesfull', 'code': 200},
            status= status.HTTP_200_OK
        )
              
#User profile Viewset
class UserProfileViewset(viewsets.ViewSet):
    
    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = ProfileSerializer(queryset, many= True)

        if not serializer.data:
            return Response(
                    {'details': 'there are no profiles', 'code': 200},
                    status.HTTP_200_OK
            )
        else:
            return Response(
                {'details': serializer.data, 'code': 200},
                status=status.HTTP_200_OK
            )
        

    def create(self, request):
        user = request.data.get('user')

        if not CustomUser.objects.filter(id = user).exists():
            return Response(
                    {'details': 'Could not find the user', 'code': 400},
                    status.HTTP_400_BAD_REQUEST
                ) 
        else:
            if UserProfile.objects.filter(user = user).exists():
                return Response(
                        {'details': 'This user already has a profile', 'code': 400},
                        status.HTTP_400_BAD_REQUEST
                    ) 
            serializer = ProfileSerializer(data = request.data, partial=True)
            if not serializer.is_valid():
                return Response(
                    {'details': serializer.errors, 'code': 400},
                    status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {'details': 'Profile added succesfully', 'code': 200},
                status = status.HTTP_200_OK
            )

    def retrieve(self, request, pk = None):
        
        try:
            # check if the user exists.
            profile = UserProfile.objects.get(id = pk)
        except UserProfile.DoesNotExist:
            return Response(
                    {'detail': 'User Profile Does not exist', 'code': 400},
                        status = status.HTTP_400_BAD_REQUEST
                )
        serializer = ProfileSerializer(profile)
        return Response(
                {'details': serializer.data, 'code': 200},
                status = status.HTTP_200_OK
                )

    def update(self, request, pk):
        
        try:
            profile = UserProfile.objects.get(id = pk)
        except UserProfile.DoesNotExist:
            return Response(
                {'details': 'Could not find Profile', 'code': 400},
                status= status.HTTP_400_BAD_REQUEST
            )
          
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'details': 'Updated succefully', 'code':200},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'detail': serializer.errors, 'code':400},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def destroy(self, request, pk=id):
        UserProfile.objects.get(pk=pk).delete()
        return Response(
            {'details': 'Delete Succesfull', 'code': 200},
            status= status.HTTP_200_OK
        )

