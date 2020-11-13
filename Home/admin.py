from django.contrib import admin
from . import models

@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'English_name')
    list_filter = ('name', 'English_name')
    search_fields = ('name', 'English_name')