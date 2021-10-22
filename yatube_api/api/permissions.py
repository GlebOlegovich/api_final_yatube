from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == "GET"


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object / admin
    to edit it.
    """
    def has_object_permission(self, request, view, obj):
        print(request)
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
        в формате tuple(кортеж)/list(список).
    '''
    add_permissions = our_viewset.need_to_add_perm
    if add_permissions:
        result = [permission() for permission in add_permissions]
    else:
        result = [ReadOnly()]
        raise TypeError('need_to_add_perm - пуст!')
    result += [
        permission() for permission
        in super(our_viewset.__class__, our_viewset).permission_classes
    ]
    return result
