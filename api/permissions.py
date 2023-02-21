from rest_framework.permissions import BasePermission
from .models import UsuarioModel

class SoloAdministradores(BasePermission):
    message ='solamente los administradores pueden realizar esra accion'

    def has_permission(self, request, view):
        print(request.user)
        usuario:UsuarioModel = request.user

        print(request.auth)
        print(usuario.tipoUsuario)
        if usuario.tipoUsuario == 'ADMINISTRADOR':
            return True

        else:
            return False

class SoloClientes(BasePermission):
    message ='puedes ver la cartilla'

    def has_permission(self, request, view):
        usuario:UsuarioModel = request.user
        if usuario.tipoUsuario == 'CLIENTE':
            return True
        else:
            return False