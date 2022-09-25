from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owner to edit objects
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any requests
        # so, GET, HEAD, or OPTIONS requests are allowed to anyone.
        if request.method is permissions.SAFE_METHODS:
            # SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
            return True

        # write permissions are allowed only to owners of the objects
        else:
            return obj.owner == request.user
