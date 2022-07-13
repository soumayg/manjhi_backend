from django.db import models

from geography.models import Country, State, District, Area

class User(models.Model):
    mobile_number = models.CharField(max_length=10, verbose_name='Mobile Number', primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Name')
    def __str__(self):
        return self.name

class UserAddressDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User Profile')
    address = models.CharField(max_length=100, verbose_name='Address')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Local Area')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')

class UserFamilyDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User Profile')
    no_baby = models.PositiveIntegerField(verbose_name='Baby')
    no_children = models.PositiveIntegerField(verbose_name='Children')
    no_adult = models.PositiveIntegerField(verbose_name='Adult')
    no_senior = models.PositiveIntegerField(verbose_name='Senior Citizen')
    no_ph = models.PositiveIntegerField(verbose_name='Physically Handicapped')
