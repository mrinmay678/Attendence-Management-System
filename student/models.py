from django.db import models
from authentication.models import CustomUser
from teacher.models import Teacher
from datetime import datetime

class Student(models.Model):
    dept=(
        ("CSE","CSE"),
        ("IT","IT"),
        ("ECE","ECE"),
        ("EE","EE"),
        ("ME","ME"),
        ("BME","BME"),
        ("CE","CE"),
    )
    batches=(
        (datetime.now().year,datetime.now().year),
        (datetime.now().year+1,datetime.now().year+1),
        (datetime.now().year+2,datetime.now().year+2),
        (datetime.now().year+3,datetime.now().year+3),
        (datetime.now().year+4,datetime.now().year+4),
    )
    years=(
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    )
    if datetime.now().month>6:
        sems=(
            ('1st','1st'),
            ('3rd','3rd'),
            ('5th','5th'),
            ('7th','7th'),
        )
    else:
        sems=(
            ('2nd','2nd'),
            ('4th','4th'),
            ('6th','6th'),
            ('8th','8th'),
        )
    user=models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=255,blank=False)
    department=models.CharField(choices=dept,max_length=30,blank=False)
    mentor=models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)
    batch=models.IntegerField(choices=batches,blank=False)
    year=models.CharField(choices=years,max_length=3,blank=False)
    semester=models.CharField(choices=sems,max_length=3,blank=False)

    def __str__(self) -> str:
        return self.name + "_" + self.user.jis_id