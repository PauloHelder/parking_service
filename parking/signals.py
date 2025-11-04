from django.db.models.signals import post_save
from django.dispatch import receiver

from parking.models import ParkingRecord

@receiver(post_save, sender=ParkingRecord)
def handle_parking_record_save(sender, instance, created, **kwargs):
    parking_spot = instance.parking_spot
    parking_spot.is_occupied = instance.exit_time is None
    parking_spot.save()
    


