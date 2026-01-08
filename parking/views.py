from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets

from core.permissions import IsOwnerOfvehicleOrRecord
from parking.models import ParkingSpot,ParkingRecord
from parking.serializers import ParkingSpotSerializer,ParkingRecordSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset=ParkingSpot.objects.all()
    serializer_class=ParkingSpotSerializer
    permission_classes=[DjangoModelPermissions]


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset=ParkingRecord.objects.all()
    serializer_class=ParkingRecordSerializer
    permission_classes=[DjangoModelPermissions, IsOwnerOfvehicleOrRecord]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)