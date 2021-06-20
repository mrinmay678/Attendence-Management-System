from django.db import models
from authentication.models import CustomUser
from teacher.models import Teacher

class Student(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=255,blank=False)
    department=models.CharField(max_length=30,blank=False)
    mentor=models.ForeignKey(Teacher, blank=False, on_delete=models.CASCADE)
    batch=models.IntegerField(blank=False)
    year=models.CharField(max_length=3,blank=False)
    semester=models.CharField(max_length=3,blank=False)