from django.db import models
from vehicles.models import Vehicle

class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Número da Vaga',
    )
    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Está Ocupado',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.spot_number
    

class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo',
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga',
    )
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name='Hora de Entrada')
    exit_time = models.DateTimeField(blank=True, null=True, verbose_name='Hora de Saída')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return f'Entrada do {self.vehicle} na vaga {self.parking_spot} - {self.entry_time}'