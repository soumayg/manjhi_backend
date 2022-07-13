from django.db import models

from user.models import User
from geography.models import Country, State, District, Area

class Disaster(models.Model):
    name = models.CharField(max_length=30, verbose_name='Type of Disaster', primary_key=True)
    def __str__(self):
        return self.name

class EssentialService(models.Model):
    name = models.CharField(max_length=30, verbose_name='Service', primary_key=True)
    def __str__(self):
        return self.name

class UserHelpRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User Profile')
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE, verbose_name='Disaster')
    eservice = models.ForeignKey(EssentialService, on_delete=models.CASCADE, verbose_name='Essential Service')
    request = models.TextField()
    is_emergency = models.BooleanField(default=False, verbose_name='Emergency')
    is_progress = models.BooleanField(default=False, verbose_name='In-Progress')
    is_complete = models.BooleanField(default=False, verbose_name='Complete')
    timestamp = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Area')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')


class EmergencyContactPoint(models.Model):
    organization = models.CharField(max_length=60, verbose_name='Organization')
    contact_number = models.CharField(max_length=15, verbose_name='Contact Number')
    is_active = models.BooleanField(default=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Area', blank = True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District', blank = True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State', blank = True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country', blank = True, null=True)
