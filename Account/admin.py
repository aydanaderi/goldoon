from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_filter = ('username','email')
    search_fields = ('username','email')