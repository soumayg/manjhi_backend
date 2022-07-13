from dataclasses import field
from rest_framework import serializers

from disaster_management import models
from user.models import User, UserAddressDetails


class DisasterSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Disaster
        fields = '__all__'


class EssentialServiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.EssentialService
        fields = '__all__'
    

class UserHelpRequestSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.UserHelpRequest
        fields = ['user','disaster','eservice','request','is_emergency']
    
    def create(self, validated_data):
        address = UserAddressDetails.objects.get(user=validated_data['user'])
        help_request = models.UserHelpRequest.objects.create(
            user = validated_data['user'],
            disaster = validated_data['disaster'],
            eservice = validated_data['eservice'],
            request = validated_data['request'],
            is_emergency = validated_data['is_emergency'],
            is_progress = False,
            is_complete = False,
            area = address.area,
            district = address.district,
            state = address.state,
            country = address.country,
        )
        return help_request

class UserHelpRequestListSerailzer(serializers.ModelSerializer):
    class Meta:
        model = models.UserHelpRequest
        fields = ['disaster','eservice','request','is_emergency','is_progress','is_complete']


class EmergencyHelpLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmergencyContactPoint
        fields = ['organization','contact_number']