from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from . import serializers,models

@api_view(['POST'])
def Signup(request):
    password = request.data['password']
    password2 = request.data['password2']
    serialized = serializers.UserSerializer(data = request.data)
    if serialized.is_valid():
        if password == password2:
            serialized.save()
            data = "successfull"
        else:
            data = "tow password did not match"
    else :
        data = "some thing was wrong"
    return Response(data)

