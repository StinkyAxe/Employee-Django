from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Extraactivity(models.Model):
    id=models.IntegerField(primary_key=True)
    ten_details = models.TextField()
    twelve_details = models.TextField()
    graduation_details = models.CharField(max_length=400)