from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken 

from . import serializers, models, permissions


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class LoginViewSet(viewsets.ViewSet):
    """
    Checks email and password and returns an auth token
    """

    serializer_class = AuthTokenSerializer

    def create (self, request):
        """
        Use the ObtainAuthToken APIView to validate and create a token
        """

        return ObtainAuthToken().post(request)

