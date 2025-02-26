from django.db import models


# Create your models here.
class RegisterModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    password = models.IntegerField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class UploadModel(models.Model):
    userDet = models.ForeignKey(RegisterModel, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    document=models.FileField()
    date=models.CharField(max_length=100)
    request = models.CharField(max_length=100, default='Pending')

class ChatModel(models.Model):
    userId = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    senderId = models.IntegerField()
    chat = models.CharField(max_length=300)

class RequestModel(models.Model):
    accessone = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    accesstwo = models.ForeignKey(UploadModel, on_delete=models.CASCADE)
    request = models.CharField(max_length=200,default='pending')

class FeedbackModel(models.Model):
    name = models.CharField(max_length=300)
    mobilenumber = models.CharField(max_length=300)
    emailid = models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

