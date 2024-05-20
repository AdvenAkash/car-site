from django.db import models


# Create your models here.
class carmodel(models.Model):
    car_name = models.CharField(max_length=50)
    car_manufacturer = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_price = models.FloatField()
    car_engine = models.CharField(max_length=10)
