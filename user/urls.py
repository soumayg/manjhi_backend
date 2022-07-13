from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view()),
    path('add/address/', views.UserAddressDetailsAPIView.as_view()),
    path('add/family/', views.UserFamilyDetailsAPIView.as_view()),
]