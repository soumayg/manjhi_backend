from rest_framework.response import Response
from rest_framework import generics, status, views

from user.models import User, UserAddressDetails
from disaster_management import serializers, models


class DisasterAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        disaster = models.Disaster.objects.all()
        serializer = serializers.DisasterSerialzer(disaster, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EssentialServiceAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        eservice = models.EssentialService.objects.all()
        serializer = serializers.EssentialServiceSerialzer(eservice, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class UserHelpRequestAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserHelpRequestSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class UserHelpRequestListAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            request_list = models.UserHelpRequest.objects.filter(user=User.objects.get(mobile_number=request.data['user']))
        except models.UserHelpRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserHelpRequestListSerailzer(request_list, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EmergencyHelpLineListAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            request_list = UserAddressDetails.objects.get(user=User.objects.get(mobile_number=request.data['user']))
        except UserAddressDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        area = models.EmergencyContactPoint.objects.filter(is_active=True).filter(area=request_list.area)
        district = models.EmergencyContactPoint.objects.filter(is_active=True).filter(district=request_list.district)
        state = models.EmergencyContactPoint.objects.filter(is_active=True).filter(state=request_list.state)
        country = models.EmergencyContactPoint.objects.filter(is_active=True).filter(country=request_list.country)
        response_dict = {}
        response_dict.update(
            {'area_name':request_list.area.name}
        )
        response_dict.update(
            {'district_name':request_list.district.name}
        )
        response_dict.update(
            {'state_name':request_list.state.name}
        )
        response_dict.update(
            {'country_name':request_list.country.name}
        )
        response_dict.update(
            {'area':serializers.EmergencyHelpLineSerializer(area, many=True).data}
        )
        response_dict.update(
            {'district':serializers.EmergencyHelpLineSerializer(district, many=True).data}
        )
        response_dict.update(
            {'state':serializers.EmergencyHelpLineSerializer(state, many=True).data}
        )
        response_dict.update(
            {'country':serializers.EmergencyHelpLineSerializer(country, many=True).data}
        )
        return Response(response_dict,status=status.HTTP_200_OK)
