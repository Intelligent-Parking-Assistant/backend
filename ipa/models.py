from django.db import models
from users.models import CustomUser
from django.db.models.deletion import CASCADE

class Parkings(models.Model):
    location = models.CharField(max_length=100)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    
    def __str__(self):
        return self.location

class Visits(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    parking = models.ForeignKey(Parkings, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.name