from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class BloodBankUserDb(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)




