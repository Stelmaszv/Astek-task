from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    added = models.DateTimeField()
    last_update=models.DateTimeField()