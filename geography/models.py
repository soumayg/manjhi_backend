from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Country')
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
    name = models.CharField(max_length=30, verbose_name='State')
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')
    name = models.CharField(max_length=30, verbose_name='District')
    def __str__(self):
        return self.name

class Area(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District')
    name = models.CharField(max_length=30, verbose_name='Area')
    def __str__(self):
        return self.name
