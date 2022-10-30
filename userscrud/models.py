
from django.db import models

class UsersCrud(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    document=models.PositiveIntegerField(max_length=20)
    age=models.IntegerField(max_length=3)
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=250)
    phone_number=models.PositiveIntegerField(max_length=15)
    profession=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name