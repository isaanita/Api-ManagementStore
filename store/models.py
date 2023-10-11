from django.db import models

# Create your models here.

class ManagementStore(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=225)
    stock = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)

def __str__(self):
    return self.name