from django.db import models
from authentication.models import CustomUser

class Teacher(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=255,blank=False)
    department=models.CharField(max_length=30,blank=False)
