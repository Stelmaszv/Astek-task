from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)
    added = models.DateTimeField(auto_now=True)
    last_update=models.DateTimeField(auto_now=True)