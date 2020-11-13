from django.urls import path
from . import views

urlpatterns = [
    path("plant/", views.CreatePlantView.as_view(),name = 'Plant'),
    path("list/", views.ListPlantView.as_view(),name = 'List'),
    path("search/", views.SearchPlantView.as_view(), name='Search')
]