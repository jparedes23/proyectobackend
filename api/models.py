from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import usuarioManager



class Productos(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table ='productos'


class Categorias(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True) 
    products = models.ManyToManyField(Productos)

    class Meta:
        db_table ='categorias'

class ProductosCategorias(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    producto_id= models.ForeignKey(Productos, on_delete=models.CASCADE)
    categoria_id= models.ForeignKey(Categorias, on_delete=models.CASCADE)

    db_table ='productos_categorias'


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[
       ('ADMIN', 'ADMINISTRADOR'),
       ('CLIENTE','CLIENTE')
    ])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    USERNAME_FIELD ='correo'
    REQUIRED_FIELDS =['nombre', 'apellido', 'tipoUsuario']


    object = usuarioManager()
    class Meta:
        db_table= 'usuarios'

