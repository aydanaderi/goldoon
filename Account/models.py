from django.db import models

class User(models.Model) :
    username =  models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    profile = models.ImageField(default = 'pic.jpg')

    def __str__(self):
        return str(self.username)