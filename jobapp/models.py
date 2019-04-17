from django.db import models

# Create your models here.
class delhijob(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()
class signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneno=models.IntegerField()
class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    feedback=models.CharField(max_length=100)
