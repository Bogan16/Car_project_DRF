from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Auto(models.Model):
    label = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.label

class AutosPassport(models.Model):
    related_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    prefix = models.CharField(max_length=2)