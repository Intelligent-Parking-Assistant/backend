from rest_framework import serializers
from .models import Parkings, Visits

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkings
        fields = "__all__"
        
class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = "__all__"