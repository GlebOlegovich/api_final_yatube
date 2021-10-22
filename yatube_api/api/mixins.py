from .permissions import set_permissions


class AddToDefaultPermissonsMixin:

    def get_permissions(self):
        return(set_permissions(self))
