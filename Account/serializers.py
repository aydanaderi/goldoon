from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User

class CreateUserSerializer(serializers.ModelSerializer):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'use correct charactors.')
    username = serializers.CharField(min_length = 5,max_length=50,validators=[alphanumeric])
    password = serializers.CharField(min_length = 8,max_length=50, validators=[alphanumeric])
    password2 = serializers.CharField(max_length = 50,validators = [alphanumeric],write_only = True)

    def validate_password(self, password,password2):

        if password != password2 :
            raise serializers.ValidationError("tow password did not match.")
        else :
            return password

    def create(self,validated_data):
        obj = super().create(validated_data)
        return obj

    class Meta :
        model = User
        fields = '__all__'