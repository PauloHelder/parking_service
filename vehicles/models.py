from django.db import models
from customers.models import Customer

# Create your models here.
class VehicleType(models.Model):
    name=models.CharField(
        max_length=50, 
        verbose_name='Tipo de Veículo',
        unique=True,
        )
    description=models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name='Tipo de Veículo'
        verbose_name_plural='Tipos de Veículos'

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de Veículos'
    )
    license_plate =models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa',
    )
    modelo=models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo',
    )
    brand=models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca',
    )
    color=models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Cor',
    )
    owner=models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicels',
        verbose_name='Proprietario'

    )
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name='Veículo'
        verbose_name_plural='Veículos'


    def __str__(self):
        return self.license_plate
