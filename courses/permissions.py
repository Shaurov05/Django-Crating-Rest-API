from rest_framework import permissions

# class UpdateOwn
class UpdateCoursePermission(permissions.BasePermission):
    """allows user to collect data only """

    def has_object_permission(self, request, view, obj):
        """ checking permissions"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return False
