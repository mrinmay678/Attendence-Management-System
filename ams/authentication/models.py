from django.db import models
from PIL import Image

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.email
    
class Candidate(models.Model):
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False)
    password = models.CharField(max_length=255, blank=False)
    pic=models.ImageField(upload_to="pic", blank=False, null=True)
    is_staff=models.BooleanField(default=False, blank=False)
    is_organization_admin = models.BooleanField(default=False, blank=False)

    def __str__(self) -> str:
        return self.email

class AdminUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.email