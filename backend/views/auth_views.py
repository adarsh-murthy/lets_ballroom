"""Define all the views for the app."""
import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)

from backend.serializers import UserSerializer


class RegisterView(APIView):
    """Allows a new user to register on the app."""

    def post(self, request):
        """Register a new user."""
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        existing_user = User.objects.filter(username=username)
        if existing_user:
            error = {'error': 'Account with username already exists.'}
            return Response(error, status=HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        user_serializer = UserSerializer(user)
        return Response({'user': user_serializer.data},
                        status=HTTP_201_CREATED)


class SignInView(APIView):
    """Allows an existing user to sign into the app."""

    def post(self, request):
        """Sign in a user."""
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            # Bad credentials
            error = {'error': 'Invalid username / password.'}
            return Response(error, status=HTTP_401_UNAUTHORIZED)
        user_serializer = UserSerializer(user)
        return Response({'user': user_serializer.data}, status=HTTP_200_OK)
