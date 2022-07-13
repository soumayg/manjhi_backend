from rest_framework import serializers

from user import models
from geography.models import Country, State, District, Area

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserAddressDetailsSerializer(serializers.ModelSerializer):
    area = serializers.CharField()
    district = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()

    class Meta:
        model = models.UserAddressDetails
        fields = '__all__'

    def create(self, validated_data):
        try:
            country = Country.objects.get(name=validated_data['country'])
        except Country.DoesNotExist:
            country = Country.objects.create(
                name = validated_data['country']
            )
            country.save()

        try:
            state = State.objects.filter(country=country).get(name=validated_data['state'])
        except State.DoesNotExist:
            state = State.objects.create(
                country = country,
                name = validated_data['state']
            )
            state.save()

        try:
            district = District.objects.filter(state=state).get(name=validated_data['district'])
        except District.DoesNotExist:
            district = District.objects.create(
                state = state,
                name = validated_data['district']
            )
            district.save()

        try:
            area = Area.objects.filter(district=district).get(name=validated_data['area'])
        except Area.DoesNotExist:
            area = Area.objects.create(
                district = district,
                name = validated_data['area']
            )
            area.save()

        address = models.UserAddressDetails.objects.create(
            user = validated_data['user'],
            address = validated_data['address'],
            area = area,
            district = district,
            state = state,
            country = country,
        )
        address.save()

        return address

    
class UserFamilyDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserFamilyDetails
        fields = '__all__'
