from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Uploaddocuments(models.Model):
    id=models.IntegerField(primary_key=True)
    ten_x = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'])],upload_to='media/%Y/%m/%d/',null=True) #for uploading Class 10 marksheet
    twelve_xii = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'])], upload_to='media/%Y/%m/%d/',null=True) #for uploading class 12 marksheet
    graduate = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc',])],upload_to='media/%Y/%m/%d/') #for uploading graduation marksheet
    photo = models.ImageField(upload_to='media/%Y/%m/%d/') #for uploading photo
