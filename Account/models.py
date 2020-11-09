from django.db import models

class Information(models.Model) :
    id = models.AutoField(primary_key=True)
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    date = models.DateTimeField()
    profile = models.ImageField(default = 'pic.jpg')

    def __str__(self):
        return str(self.username)