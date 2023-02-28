from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView
from .models import Categorias, Productos, ProductosCategorias, UsuarioModel
from . serializers import CategoriaSerializer, ProductoSerializer, ProductosCategoriaSerializers, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import SoloAdministradores


class CategoriaApiView(ListCreateAPIView):
     permission_classes =[IsAuthenticated, SoloAdministradores]
     queryset = Categorias.objects.all()
     serializer_class = CategoriaSerializer



class ProductoApiView(ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
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


class ListarCategoriaApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, SoloAdministradores]

    def get(self, request:Request, pk : int):
        categoriaEncontrada = Categorias.objects.filter(id= pk).first()
        print(categoriaEncontrada)

        if categoriaEncontrada is None:
            return Response(data={
                'message': 'Categoria no existe'
            })
        # dir(instancia) > nos muestra todos los atributos y metodos de la clase
        # print(dir(categoriaEncontrada))
        
        # SELECT * FROM platos WHERE categoria_id = ... AND id = 10;
        print(categoriaEncontrada.productoscategorias_set.all())
        categoria = categoriaEncontrada.pproductoscategorias_set.all() # estamos accediendo al primer plato de esta categoria
        print(categoria.nombre)
        print(categoria.id)

        serializador = ProductosCategorias(instance=categoriaEncontrada)


        return Response(data={
            'content': serializador.data
        })
    
    def delete(self, request: Request, pk: int):
        print(pk)
        categoriaEncontrada = Productos.objects.filter(id = pk).first()

        if categoriaEncontrada is None:
            return Response(data={
                'message': 'La categoria no existe'
            })
        
        categoriaEncontrada.delete()
        categoriaEncontrada.save()

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
        })

    
class ListarProductoApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, SoloAdministradores]
    def get(self, request:Request, pk : int):
        # SELECT * FROM CATEGORIAS WHERE ID = ... LIMIT 1;
        productoEncontrada = Productos.objects.filter(id= pk).first()
        print(productoEncontrada)

        if productoEncontrada is None:
            return Response(data={
                'message': 'Productos no existe'
            })
        print(productoEncontrada.productoscategorias_set.all())
        # producto = productoEncontrada.productoscategorias_set.all()
        # print(producto.nombre)
        # print(producto.id)
        # print(producto.precio)
  

        serializador = ProductoSerializer(instance=productoEncontrada)


        return Response(data={
            'content': serializador.data
        })

  
    def delete(self, request: Request, pk: int):
        print(pk)
        productoEncontrado = Productos.objects.filter(id = pk, disponibilidad = True).first()

        if productoEncontrado is None:
            return Response(data={
                'message': 'El producto no existe'
            })
        
        productoEncontrado.disponibilidad = False
        productoEncontrado.save()

        return Response(data={
            'message': 'Producto eliminado exitosamente'
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

