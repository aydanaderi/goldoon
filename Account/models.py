from django.core.validators import RegexValidator
from django.db import models

class User(models.Model) :
    username =  models.CharField(max_length = 50,unique = True)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'use correct charactors.')
    password = models.CharField(max_length = 50,validators = [alphanumeric])
    email = models.EmailField(max_length = 100)
    profile = models.ImageField(default = 'pic.jpg',null = True,blank = True)

    def __str__(self):
        return str(self.username)