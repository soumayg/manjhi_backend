from django.urls import path
from disaster_management import views

urlpatterns = [
    path('disaster/', views.DisasterAPIView.as_view()),
    path('essential-services/', views.EssentialServiceAPIView.as_view()),
    path('request/add/', views.UserHelpRequestAPIView.as_view()),
    path('request/', views.UserHelpRequestListAPIView.as_view()),
    path('request/call/', views.EmergencyHelpLineListAPIView.as_view()),
]