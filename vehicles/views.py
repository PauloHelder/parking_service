from rest_framework import viewsets

from vehicles.models import VehicleType,Vehicle
from vehicles.serializers import VehicleTypeSerializer,VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset=VehicleType.objects.all()
    serializer_class=VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer