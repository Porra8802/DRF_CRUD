from pyexpat import model
from django.db import models

class ReadExcel(models.Model):
    A=models.IntegerField(max_length=100)
    B=models.IntegerField(max_length=100)
    C=models.IntegerField(max_length=100)
    D=models.IntegerField(max_length=100)
    E=models.IntegerField(max_length=100)