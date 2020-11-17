from django.urls import path,include
from knox import views as knox_views
from . import views

urlpatterns = [
    path('signup/', views.RegisterAPI.as_view(), name = 'register'),
    path('login/', views.LoginAPI.as_view(), name = 'login'),
    path('logout/', knox_views.LogoutView.as_view(), name = 'logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name = 'change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace = 'password_reset')),
]
