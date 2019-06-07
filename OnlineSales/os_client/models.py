from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30)
    contactno = models.IntegerField()
    photo = models.ImageField(upload_to="client/")
    address = models.TextField()
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()


class Complaint(models.Model):
    no = models.AutoField(primary_key=True)
    client_un = models.ForeignKey(Client,on_delete=models.CASCADE)
    comment = models.TextField()

