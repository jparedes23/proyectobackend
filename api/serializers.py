from rest_framework import serializers
from .models import Productos, Categorias, ProductosCategorias

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

