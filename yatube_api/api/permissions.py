from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == "GET"


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object / admin
    to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_superuser
        )


def set_permissions(our_viewset):
    '''
        Функция для получения пермишнс - берем дефолтные и добавляем те,
        которые нам нужны. Те пермишны, которые хотим добавить к
        дефолтным - прописываем в переменной need_to_add_perm в нашем вьюсете,
        в формате tuple(кортеж).
    '''
    result = [ReadOnly()]
    try:
        add_permissions = our_viewset.need_to_add_perm
        if isinstance(add_permissions, tuple):
            result = [permission() for permission in add_permissions]
        else:
            raise TypeError('need_to_add_perm должен быть кортежем')
        result += super(our_viewset.__class__, our_viewset).get_permissions()
    except Exception as error:
        raise error
    return result
