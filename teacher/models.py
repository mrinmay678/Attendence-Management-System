from django.db import models
from authentication.models import CustomUser

class Teacher(models.Model):
    dept=(
        ("CSE","CSE"),
        ("IT","IT"),
        ("ECE","ECE"),
        ("EE","EE"),
        ("ME","ME"),
        ("BME","BME"),
        ("CE","CE"),
        ("PHY","PHY"),
        ("CHEM","CHEM"),
        ("MATHS","MATHS")
    )
    user=models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=255,blank=False)
    department=models.CharField(choices=dept,max_length=30,blank=False)

    def __str__(self) -> str:
        return self.name + "_" + self.user.jis_id