from django.db import models

class User(models.Model):
    name = models.CharField('Nombre del usuario',max_length=100)
    email = models.CharField('Email del usuario',max_length=100)
    birth_date = models.DateField()
    car = models.ForeignKey('Car',on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.name} - {self.email} - {self.car.id}'
    