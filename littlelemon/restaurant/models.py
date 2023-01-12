from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()

class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self) -> str:
        return self.title