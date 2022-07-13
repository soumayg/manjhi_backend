from rest_framework.response import Response
from rest_framework import generics, status, views

from user import serializers

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserAddressDetailsAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserAddressDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UserFamilyDetailsAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserFamilyDetialsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
