from rest_framework import serializers
from .models import User

class CreateUserSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if len(data.get('username')) < 5 :
            raise serializers.ValidationError("username is too short")
        elif len(data.get('password')) < 8 :
            raise serializers.ValidationError("password is too common")
        else :
            return data

    class Meta :
        model = User
        fields = '__all__'