from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    weight=models.IntegerField(max_length=50)
    price=models.IntegerField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)