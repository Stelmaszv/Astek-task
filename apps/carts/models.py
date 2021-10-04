from django.db import models

import datetime


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(null=True)
    added = models.DateTimeField(auto_now_add=True,blank=False)
    last_update=models.DateTimeField(auto_now=True)
    dishs = models.ManyToManyField(to='carts.Dish', related_name='Dish',blank=True)

    def save(self, *args, **kwargs):
        self.last_update=datetime.datetime.now()
        super(Cart, self).save(*args, **kwargs)

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
    cart_id     = models.ForeignKey(
        to='carts.Cart',
        on_delete=models.CASCADE,
        related_name='Cart',null=True
    )

    def __str__(self):
        return str(self.id)+', '+self.name+', '+self.description+', '+str(self.price)
