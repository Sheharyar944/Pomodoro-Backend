from django.shortcuts import render
from .models import User
from rest_framework import permissions, viewsets
from .serializers import  UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer  # Mak
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    def post(self, request, format=None):
        response = super().post(request, format)
        if response.status_code == 200:
            user = authenticate(email=request.data['email'], password=request.data['password'])
            refresh = RefreshToken.for_user(user)
            response.data['refresh_token'] = str(refresh)
            # Pass request context to the serializer
            response.data['user'] = UserSerializer(user, context={'request': request}).data
        return response

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
