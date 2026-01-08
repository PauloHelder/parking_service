from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets

from core.permissions import IsOwnerOfvehicleOrRecord
from vehicles.models import VehicleType,Vehicle
from vehicles.serializers import VehicleTypeSerializer,VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset=VehicleType.objects.all()
    serializer_class=VehicleTypeSerializer
    permission_classes=[DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    permission_classes=[DjangoModelPermissions, IsOwnerOfvehicleOrRecord]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.customer)