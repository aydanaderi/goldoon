from rest_framework import generics,filters
from . import models
from .serializers import CreatePlantSerializer,ListPlantSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class CreatePlantView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = models.Plant.objects.all()
    serializer_class = CreatePlantSerializer

class SearchPlantView(generics.ListAPIView):
    permission_classes = [IsAdminUser,IsAuthenticated]
    queryset = models.Plant.objects.all()
    serializer_class = ListPlantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','English_name']
