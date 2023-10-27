from rest_framework.permissions import BasePermission


class IsSchoolAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.school == obj


class IsSchoolTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.user.school == obj
        except:
            return request.user.school == obj.
