from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    phone=models.CharField(max_length=20)
    street_address=models.CharField(max_length=200)


class Profile(models.Model):
    user=models.OneToOneField(CustomUserModel,related_name="profile",on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="profile_picture")
    bio=models.TextField()
    dob=models.DateField(null=True)
    date=models.DateField(auto_now=True)