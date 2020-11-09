from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from . import serializers,models

@api_view(['POST'])
def Signup(request):
    username = request.data['username']
    password = request.data['password']
    password2 = request.data['password2']
    serialized = serializers.UserSerializer(data = request.data)
    data = {}
    if serialized.is_valid():
        for u in models.User.objects.all() :
            if str(u.username) == str(username) :
                data['respone'] = "this username exists!"
                return Response(data)
        if password == password2:
            user = serialized.save()
            data['respone'] = user.username + " signed up!"
        else:
            data['respone'] = "tow password did not match"
    else :
        data['respone'] = "some thing was wrong"
    return Response(data)

