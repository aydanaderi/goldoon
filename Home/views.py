from rest_framework import generics,filters
from . import models
from .serializers import CreatePlantSerializer,SearchPlantSerializer,ListPlantSerializer
from rest_framework.permissions import IsAdminUser

class CreatePlantView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = models.Plant.objects.all()
    serializer_class = CreatePlantSerializer

class ListPlantView(generics.ListAPIView):
    queryset = models.Plant.objects.all()
    serializer_class = ListPlantSerializer

class SearchPlantView(generics.ListAPIView):
    queryset = models.Plant.objects.all()
    serializer_class = SearchPlantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','English_name']