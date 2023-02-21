from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView
from .models import Categorias, Productos, ProductosCategorias, UsuarioModel
from . serializers import CategoriaSerializer, ProductoSerializer, ProductosCategoriaSerializers, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloAdministradores, SoloClientes


class CategoriaApiView(ListCreateAPIView):
     permission_classes =[IsAuthenticated, SoloAdministradores]
     queryset = Categorias.objects.all()
     serializer_class = CategoriaSerializer


class ProductoApiView(ListCreateAPIView):
    queryset = Productos.objects.all()

    def get(self, request: Request):
        resultado = Productos.objects.all()
        print(resultado)

        serializador = ProductoSerializer(instance=resultado, many= True)
        print(serializador.data)

        return Response(data={
            'content': serializador.data
        })

    def post (self, request: Response):
        body = request.data

        serializador = ProductoSerializer(data=body)
        valida = serializador.is_valid()

        productoExistente = Productos.objects.filter(nombre = body.get('nombre')).first()

        if productoExistente :
            return Response(data={
                'message' : 'El producto {} ya existe'.format(productoExistente.nombre)
            })

        if valida == False:
            return Response(data={
                'message': 'La informacion es invalida',
                'content': serializador.errors
            })
        
        print(serializador.validated_data)

        nuevoProducto = serializador.save()
        print(nuevoProducto)

        serializar = ProductoSerializer(instance=nuevoProducto)

        return Response(data={
            'message': 'Producto creado exitosamente',
            'content':serializar.data
        })


class RegistroUsuarioApiView(CreateAPIView):
    def post(self, request: Request):
        serializador = RegistroUsuarioSerializer(data = request.data)
        validacion = serializador.is_valid()

        if validacion is False:
            return Response(data={
                'message': 'error al crear el usuario',
                'content': serializador.errors
            }, status=400)
        
        # inicializo el nuevo usuario con la informacion validada
        nuevoUsuario = UsuarioModel(**serializador.validated_data)
        # ahora genero el hash de la contraseña
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        # guardo el usuario en la base de datos
        nuevoUsuario.save()

        return Response(data={
            'message': 'Usuario creado exitosamente'
        }, status=201)

