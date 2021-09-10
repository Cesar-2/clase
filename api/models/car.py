from django.db import models


class Car(models.Model):
    number_plate = models.CharField(max_length=6)
    model = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.number_plate} - {self.branch}'

