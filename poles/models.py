from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=0)
    summary = models.CharField(max_length=300)
    totalExperience = models.IntegerField(default=1)
    cCTC = models.DecimalField(decimal_places=2, max_digits=9)
    eCTC = models.DecimalField(decimal_places=2, max_digits=9)



class Company(models.Model):
    profile = models.ForeignKey(Profile, on_delete=0)
    companyName = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    designation = models.CharField(max_length=50)
    contribution = models.CharField(max_length=500)

