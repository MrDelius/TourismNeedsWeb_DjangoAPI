from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read permissions for all authenticated users (GET, HEAD, OPTIONS requests)
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        # Allow full permissions for admins (staff users)
        return request.user.is_staff


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_staff
        is_owner = obj.user
        is_owner_or_admin = (obj.user == request.user) or is_admin or (obj == request.user)

        return is_owner_or_admin


