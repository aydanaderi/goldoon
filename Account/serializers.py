from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = models.User
        fields = ['username','password','password2','email']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self):
        user = models.User.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.password = password
        user.save()
        return user

