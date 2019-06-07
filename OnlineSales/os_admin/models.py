from django.db import models

class AdminLogin(models.Model):
    contactno = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()


class Agent(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='agent/')
    address = models.TextField()
    contactno = models.IntegerField()
    username = models.CharField(primary_key=True,max_length=30)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()

