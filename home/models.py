from django.db import models

# Create your models here.

class Cricketers(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    email = models.EmailField(null = True , blank = True)
    address = models.TextField( null = True , blank = True )
    runs = models.IntegerField()
    # image = models.ImageField()(null=True, blank= True )


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)

    def __str__(self) ->str:
        return self.car_name