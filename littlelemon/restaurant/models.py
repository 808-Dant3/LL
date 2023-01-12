from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()
    def __str__(self) -> str:
        return self.title

class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self) -> str:
        return self.title

class user(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    groups = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.title