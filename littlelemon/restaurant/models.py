from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    number_of_guests = models.IntegerField(null=False)

    def __str__(self):
        return self.name + ' - ' + str(self.reservation_date)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(null=False)

    def __str__(self):
        return self.title