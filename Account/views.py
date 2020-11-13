from rest_framework import generics
from . import models
from .serializers import CreateUserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = CreateUserSerializer
    lookup_field = id

