from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return self.name
    

class Car(models.Model):
    carName = models.CharField(max_length=200)
    transmision=models.CharField(max_length=200)
    def __str__(self):
        return self.carName