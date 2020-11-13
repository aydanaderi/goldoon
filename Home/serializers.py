from rest_framework import serializers
from .models import Plant

class CreatePlantSerializer(serializers.ModelSerializer):

    class Meta :
        model = Plant
        fields = '__all__'