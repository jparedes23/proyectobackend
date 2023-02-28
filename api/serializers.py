from rest_framework import serializers
from .models import Productos, Categorias, ProductosCategorias, UsuarioModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields = '__all__'


class ProductosCategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductosCategorias
        fields= '__all__'

class MostrarProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'
        depth = 1
class CrearProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'
        
class EliminarProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsuarioModel
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
