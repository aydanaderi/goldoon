from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'use correct charactors.')
    username =  serializers.CharField(min_length = 5,max_length = 50,validators = [alphanumeric])
    password = serializers.CharField(min_length = 8,max_length = 50,validators = [alphanumeric])
    profile = serializers.ImageField(default = 'pic.jpg')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','profile')
        extra_kwargs = {'password': {'write_only': True},'profile': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)

class ResetPasswordSerializer(serializers.Serializer):
    class Meta:
        model = models.User
        fields = ('username', 'email')

class ConfirmResetPasswordSerializer(serializers.Serializer):
    model = User
    password = serializers.CharField(required = True)

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email','profile')