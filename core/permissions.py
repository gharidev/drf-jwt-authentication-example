from rest_framework.permissions import BasePermission

class AllowInternalUsers(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.email.split("@")[1] == "beinex.com"
