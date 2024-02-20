from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser as User
from rest_framework.permissions import AllowAny
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from .serializers import UserSerializer, UserProfileSerializer, CustomPasswordResetSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
"""
Generate Token Manually
"""
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"token":token, "message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserProfileSerializer(user)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomPasswordResetView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = CustomPasswordResetSerializer(data = request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Password reset successfully"}, status=status.HTTP_200_OK)
        return Response({"error":"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
class SendPasswordResetEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Password reset email sent successfully"}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uidb64, 'token': token})
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Password reset successfully", "user_id": user.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)