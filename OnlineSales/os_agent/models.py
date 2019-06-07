from django.db import models
from os_admin.models import Agent
from os_client.models import Client

class Property(models.Model):
    no = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="property/")
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    facing = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    add_date = models.DateField(auto_now_add=True)
    sold_date = models.DateField(auto_now_add=True)

class SoldProperty(models.Model):
    property_no = models.ForeignKey(Property,on_delete=models.CASCADE)
    client_un = models.ForeignKey(Client,on_delete=models.CASCADE)
    date_of_sold = models.DateField(auto_now_add=True)

class BlockProperty(models.Model):
    no = models.AutoField(primary_key=True)
    property_no = models.ForeignKey(Property,on_delete=models.CASCADE)
    block_date = models.DateField(auto_now_add=True)
    client_un = models.ForeignKey(Client, on_delete=models.CASCADE)
