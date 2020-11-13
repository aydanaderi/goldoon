from rest_framework import generics
from . import models
from .serializers import CreatePlantSerializer
from rest_framework.permissions import IsAdminUser

class CreatePlantView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = models.Plant.objects.all()
    serializer_class = CreatePlantSerializer
    lookup_field = id

