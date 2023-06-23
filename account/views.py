from django.shortcuts import render
from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import UserRegisterSerializer, UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

from account.renderer import UserRenderer


# Create your views here.


# Generate  Jwt token Manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Register successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class UserLoginView(APIView):
    
    

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            check_user = authenticate(email=email, password=password)

            if check_user is not None:
                token = get_tokens_for_user(check_user)
                return Response({'token': token, 'msg': "Login Successfully"}, status=status.HTTP_200_OK)
            return Response({'nonfieldserror': {'Invalid Email or Password'}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class UserChangePasswordView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    
    def post(self, request,format=None):
        serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})

        if serializer.is_valid():
            return Response({'msg':'User changed password successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class UserLogoutView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes=[IsAuthenticated]
#     def get(self, request,format=None):
#          request.user.auth_token.delete()

#          logout(request)

#          return Response('User Logged out successfully')

    