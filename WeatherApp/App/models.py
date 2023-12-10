from django.db import models

class Weather(models.Model):
    city=models.CharField(max_length=200)


