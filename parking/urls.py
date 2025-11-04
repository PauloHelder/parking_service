from django.urls import path,include
from rest_framework.routers import DefaultRouter

from parking.views import ParkingSpotViewSet, ParkingRecordViewSet

router =DefaultRouter()
router.register('parking/spots', ParkingSpotViewSet) 
router.register('parking/records', ParkingRecordViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]