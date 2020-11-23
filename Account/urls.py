from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('signup/', views.RegisterAPI.as_view(), name = 'register'),
    path('login/', views.LoginAPI.as_view(), name = 'login'),
    path('logout/', knox_views.LogoutView.as_view(), name = 'logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name = 'change-password'),
    path('reset/', views.ResetPasswodView, name = 'reset'),
    path('<int:username_id>/reset/confirm/', views.ConfirmResetPasswodView , name = 'Reset_password')
]
