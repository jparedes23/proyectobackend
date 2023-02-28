from django.urls import path
from .views import CategoriaApiView, ProductoApiView, RegistroUsuarioApiView,  ListarCategoriaApiView, ListarProductoApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('categoria/', CategoriaApiView.as_view()),
    path('producto/', ProductoApiView.as_view()),
    path('registro/', RegistroUsuarioApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('producto/<int:pk>', ListarProductoApiView.as_view()),
    path('categoria/<int:pk>', ListarCategoriaApiView.as_view()),
]
