from django.db import models

class User(models.Model) :
    username =  models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 200)
    profile = models.ImageField(default = 'pic.jpg',null = True,blank = True)

    def __str__(self):
        return str(self.username)