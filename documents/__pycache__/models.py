from django.db import models
from django.contrib.auth.models import User
from .index import models
# Create your models here.
class Documents(models.Model):
    id = models.models.ForeignKey("index.Model",on_delete=models.CASCADE)
    roll_x = models.IntegerField()
    board_x = models.CharField(max_length=50)
    school_x = models.CharField(max_length=50)
    percentage_x = models.IntegerField()
    roll_xii = models.IntegerField()
    board_xii = models.CharField(max_length=50)
    school_xii = models.CharField(max_length=50)
    percentage_xii = models.IntegerField()
    degree_name = models.CharField(max_length = 20)
    univ_name = models.CharField(max_length = 50)
    college_name = models.CharField(max_length = 50)
    univ_roll = models.IntegerField()
    percentage = models.IntegerField()