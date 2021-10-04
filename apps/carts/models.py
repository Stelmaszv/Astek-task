from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    added = models.DateTimeField()
    last_update=models.DateTimeField()