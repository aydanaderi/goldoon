from django.urls import path
from . import views

urlpatterns = [
    path("create_auth/", views.create_auth)
]