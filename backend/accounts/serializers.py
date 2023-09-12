from rest_framework import serializers
# from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import Permissions
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['username']  = user.username
        token['role'] = user.role
        token['admin'] = user.admin
        token['active'] = user.active
        token['account_type'] = user.account_type
        token['suspended'] = user.suspended
        token['verified'] = user.verified
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        
        return token

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'phone_number',
                  'username', 'role', 'admin', 'active', 'suspended', 'verified', 
                  'account_type', 'first_name', 'last_name'
                  )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                     message='This email is already taken')]
    )
    # phone_number = serializers.CharField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all(),
    #                                     message='This phone number is already taken')]
    # )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','password', 'email', 'phone_number', 'account_type',
                  'role', 'admin', 'active', 'suspended', 'verified',
                  'first_name', 'last_name')
                  
        extra_kwargs = {
            'last_name': {'required': False},
            'id': {'read_only': True}
        }


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            admin=validated_data['admin'],
            active=validated_data['active'],
            suspended=validated_data['suspended'],
            verified=validated_data['verified'],
            account_type=validated_data['account_type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class PermissionsSerializer(serializers.Serializer):
    model = Permissions
    fields = "__all__"
