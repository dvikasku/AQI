from django.db import models

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=255)
    exp=models.CharField(max_length=100)
    any=models.CharField(max_length=100)
    rate=models.IntegerField(("10"))