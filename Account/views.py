from rest_framework import generics
from .models import User
from .serializers import CreateUserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    lookup_field = id

