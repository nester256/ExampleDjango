from rest_framework.permissions import BasePermission

class IsSafeMethod(BasePermission):
    """
    Разрешает только безопасные методы (GET, HEAD, OPTIONS) для всех пользователей.
    Для всех других методов требует аутентификацию.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated