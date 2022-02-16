from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.method in permissions.SAFE_METHODS
        if request.method in ('DELETE', 'PATCH'):
            return obj.author == request.user

        return True


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
