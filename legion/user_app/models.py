from django.db import models
from django.contrib.auth.models import User
from bikes_app.models import Bikes
# Create your models here.

class Role(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    first_name = models.CharField(blank=False, max_length=255)

    last_name = models.CharField(blank=False, max_length=255)

    owned_bike = models.ForeignKey(Bikes, on_delete=models.CASCADE, blank=True, null = True)

    owned_bike_review = models.TextField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.user.username)
