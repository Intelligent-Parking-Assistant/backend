from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models.deletion import CASCADE

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    name = models.CharField(max_length=70, null=True)
    phone = models.CharField(max_length=40, null=True)
    location = models.CharField(max_length=80, null=True)
    
    def __str__(self):
        return self.name
    
    