from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=1000,primary_key=True)
    password=models.CharField(max_length=1000)
    nickname=models.CharField(max_length=1000,default=name)
    image=models.CharField(max_length=1000,default='')

class Message(models.Model):
    value=models.CharField(max_length=100000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=1000)
    recipent=models.CharField(max_length=1000)
    xx=models.CharField(max_length=1000)
    



