from django.db import models

# Create your models here.
class GSDMODEL(models.Model):
    Characteristic = models.IntegerField(unique = True)
    GDP_in_billion = models.FloatField()

class INR(models.Model):
    rupee = models.IntegerField()

# class GSDINR(models.Model):
#     Characteristics = models.IntegerField()
#     GDP_in_billion_INR = models.FloatField()
