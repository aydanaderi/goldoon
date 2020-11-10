from django.db import models

class User(models.Model) :
    username =  models.CharField(max_length = 100,unique = True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 500)
    profile = models.ImageField(default = 'pic.jpg')

    def __str__(self):
        return str(self.username)