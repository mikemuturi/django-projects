
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    professional = models.CharField(max_length=100, blank=True)
    public_access = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
