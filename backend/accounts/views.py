from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from subsystem.models import *
from profiles.models import SchoolProfile, GuardianProfile, StudentProfile, TeacherProfile
from profiles.serializers import SchoolProfileSerializer, GuardianProfile, StudentGuardian, TeacherProfileSerializer
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
# from django.contrib.auth import get_user_model
# User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserViewAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


    @action(detail=False, methods=['post'])
    def create_account(self, request):
        # Create a new user account
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Update user profile
            profile_data = {
                'school_name': request.data.get('school_name'),
            }
            subsystem_id = request.data.get('subsystem')

            subsystem = Subsystem.objects.get(id = subsystem_id)

            account_type = request.data.get('account_type')

            print("----------------------------")
            print(account_type)
            print(profile_data)

            # Assuming SchoolProfile has a OneToOne relationship with User
            user_profile, created = SchoolProfile.objects.get_or_create(user=user, subsystem = subsystem)
            for key, value in profile_data.items():
                setattr(user_profile, key, value)
            user_profile.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutAndBlacklistRefreshToken(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        id = self.kwargs['number']
        obj = User.objects.get(phone_number=id)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)