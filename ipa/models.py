from django.db import models
from users.models import CustomUser
from django.db.models.deletion import CASCADE

class Parkings(models.Model):
    location = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    
    def __str__(self):
        return self.location

class Visits(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    parking = models.ForeignKey(Parkings, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.parking.location
    
class Free(models.Model):
    parking = models.ForeignKey(Parkings, on_delete=CASCADE)
    free = models.IntegerField(default=0)
    
    def __str__(self):
        return self.parking.location