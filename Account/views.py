from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status,generics,permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth.models import User
from knox.views import LoginView as KnoxLoginView
from django.dispatch import receiver
from django.core.mail import send_mail
from knox.models import AuthToken
from . import models,serializers

class RegisterAPI(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        models.User.objects.create(username = request.data['username'],password = request.data['password'],
                                             email = request.data['email'],profile = request.data['profile'])
        login(request, user)
        subject = "signed up"
        message = 'hello!\nyou singed up successfully'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return Response({
        "user": serializers.UserSerializer(user, context = self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format = None)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset = None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status = status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            models.User.objects.filter(username = self.request.user).update(password=serializer.data.get("new_password"))
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    subject = "Password Reset for password"
    message = 'http://127.0.0.1:8000/password_reset/confirm/' + '\nenter the '+ reset_password_token.key + ' in Token'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [reset_password_token.user.email,]
    send_mail(subject, message, email_from, recipient_list)
