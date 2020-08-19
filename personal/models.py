from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Personal(models.Model):
    id=models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    phone = models.IntegerField()
    ephone = models.IntegerField()
    address1 = models.TextField()
    address2 = models.TextField()
    flat_number = models.IntegerField()
    flat_name = models.CharField(max_length=20)
    landmark = models.CharField(max_length=30,null=False)
    pincode = models.IntegerField()