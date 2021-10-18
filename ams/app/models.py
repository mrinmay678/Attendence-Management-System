from django.db import models
from authentication.models import Organization, Candidate

# Create your models here.
class Slot(models.Model):
    name=models.CharField(max_length=200,blank=False,null=True)
    organization=models.ForeignKey(Organization, on_delete=models.CASCADE)
    candidates=models.ManyToManyField(Candidate)

    def __str__(self):
        return self.name

