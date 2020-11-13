from django.urls import path
from . import views

urlpatterns = [
    path("plant/", views.CreatePlantView.as_view(),name = 'Plant'),
    path("search/", views.SearchPlantView.as_view(), name='Search')
]