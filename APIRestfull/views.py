# Importamos los modelos
from .models import *
# Importamos la serealizacion de estos modelos
from .serializers import *
# PARA el uso del API (Defecto)
from rest_framework import viewsets

# libs para logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

# Usados en el API Personalizada USADA
from rest_framework.views import APIView
from rest_framework import generics

#lib para la documentacion
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

@api_view(['GET'])
def docs_view(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403)
    return include_docs_urls(title='Documentación API')(request)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        # Eliminar el token del usuario autenticado
        request.user.auth_token.delete()
        return Response({"Mensaje": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Grupos de Vistas definen el comportamiento de la vista.
# Revisar por cualquier duda https://codeloop.org/django-rest-framework-course-for-beginners/
#-----------------------API OER--------------------#
class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class AutoriaViewSet(viewsets.ModelViewSet):
    queryset = Autoria.objects.all()
    serializer_class = AutoriaSerializer
    
class AutoriaPersonalizadoViewSet(viewsets.ModelViewSet):
    queryset = Autoria.objects.all()
    serializer_class = AutoriaPersonalizadoSerializer
    
# #-----------------------API Personalizada USADA--------------------#
# class LibrosList(APIView): 
#     def get(self, request):
#         repository = Libros.objects.all()
#         serializer = LibrosSerializer(repository, many=True)
#         return Response(serializer.data)

# class LibrosDetails(APIView): 
#     def get_object(self, id):
#         try:
#             return Libros.objects.get(id=id)
#         except Libros.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
     
#     def get(self, request, id):
#         repository = self.get_object(id)
#         serializer = LibrosSerializer(repository)
#         return Response(serializer.data)

# class AutoresList(APIView):
#     def get(self, request):
#         Autores = Autores.objects.all()
#         serializer = AutoresSerializer(Autores, many=True)
#         return Response(serializer.data)

# class AutoresDetails(APIView): 
#     def get_object(self, id):
#         try:
#             return Autores.objects.get(id=id)
#         except Autores.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         Autores = self.get_object(id)
#         serializer = AutoresSerializer(Autores)
#         return Response(serializer.data)

