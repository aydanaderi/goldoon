from django.db import models

class Plant(models.Model) :
    amount = (
        ('low' , 'low'),
        ('middle' , 'middle'),
        ('high' , 'high'),
    )
    quantity = (
        ('low', 'low'),
        ('middle', 'middle'),
        ('high', 'high'),
    )
    answer = (
        ('yes' , 'yes'),
        ('no' , 'no'),
    )
    name = models.CharField(max_length = 500 , default = '-')
    English_name = models.CharField(max_length = 500,default = '-')
    irrigation_quantity = models.CharField(max_length = 10,choices = amount,null = True,blank = True,default = '-')
    irrigation = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    temprature_quantity = models.CharField(max_length = 500,default = '-',null = True,blank = True)
    temprature = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    light_quantity = models.CharField(max_length = 10,choices = amount,default = '-',null = True,blank = True)
    light = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    humidity_quantity = models.CharField(max_length = 10,choices = amount,default = '-',null = True,blank = True)
    humidity = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    soil = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    fertilizer = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    problems = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    potting = models.CharField(max_length = 10000,default = '-',null = True,blank = True)
    poisonous = models.CharField(max_length = 5,choices = answer,default = '-',null = True,blank = True)
    sensibility = models.CharField(max_length = 10,choices = amount,default = '-',null = True,blank = True)

    def __str__(self):
        return self.name

