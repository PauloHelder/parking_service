from rest_framework import permissions

class IsOwnerOfvehicleOrRecord(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user

        if hasattr(obj, 'Vehicle') and  hasattr(obj.vehicle, 'owner'):
            return obj.Vehicle.owner and obj.Vehicle.owner.user == user
        
        return False