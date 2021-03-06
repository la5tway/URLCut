from rest_framework.permissions import BasePermission
from rest_framework import permissions


class OwnResourcePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'create':
            return True
        return request.user or request.user.is_staff == obj.author
