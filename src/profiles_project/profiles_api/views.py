from django.shortcuts import render


from rest_framework import viewsets, status
from rest_framework.response import Response 

from . import serializers, models


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
