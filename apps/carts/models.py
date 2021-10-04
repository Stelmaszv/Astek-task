from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(null=True)
    added = models.DateTimeField(auto_now=True)
    last_update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)
    preparation_time = models.BigIntegerField(default=0)
    added = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    is_vege = models.BooleanField(default=False)

    def __str__(self):
        return self.name
