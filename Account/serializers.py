from rest_framework.serializers import ModelSerializer
from .models import User

class CreateUserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'