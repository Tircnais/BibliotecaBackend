# Que es un serializador en Django
# PASAR los datos de:
# BD: Datos -->  JSON
# JSON --> bbdd 

from rest_framework import serializers, routers, viewsets
# Importamos los modelos
from .models import *

# API Autores
class AutoresSerializer(serializers.ModelSerializer):
    # Método para incluir todos los libros del autor en un arreglo
    libros = serializers.SerializerMethodField()

    class Meta:
        model = Autores
        fields = ['id', 'nombre', 'fecha_nacimiento', 'libros']

    def get_libros(self, obj):
        # Obtener todas las relaciones de Autoria donde el autor sea el actual
        autorias = Autoria.objects.filter(fk_autor=obj)
        # Devolver una lista con los detalles del libro a través del serializador
        return LibrosSerializer(
            [autoria.fk_libro for autoria in autorias], 
            many=True, 
            context={'autorias': autorias}  # Pasamos el contexto para libros_escritos
        ).data
        
class LibrosSerializer(serializers.ModelSerializer):
    # Esta clase sigue igual, pero incluye el campo libros_escritos
    libros_escritos = serializers.IntegerField(source='autoria.libros_escritos', read_only=True)

    class Meta:
        model = Libros
        # fields = ['id', 'titulo', 'anio', 'genero', 'idioma', 'descripcion']
        fields = ['id', 'titulo', 'anio', 'genero', 'idioma', 'descripcion', 'libros_escritos']

class AutoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autoria
        fields = ['id', 'fk_autor', 'fk_libro', 'libros_escritos']

# Personalización de la tabla autoría
class AutoresPersonalizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = ['id', 'nombre', 'fecha_nacimiento']

class LibrosPersonalizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ['id', 'titulo', 'anio', 'genero', 'idioma', 'descripcion']


class AutoriaPersonalizadoSerializer(serializers.ModelSerializer):
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autores.objects.all(), source='fk_autor', write_only=True)  # Para ingresar el ID del autor
    libro_id = serializers.PrimaryKeyRelatedField(queryset=Libros.objects.all(), source='fk_libro', write_only=True)  # Para ingresar el ID del libro

    # Serializadores para mostrar información del autor y libro de forma amigable al obtener datos
    autor = AutoresPersonalizadoSerializer(source='fk_autor', read_only=True)
    libro = LibrosPersonalizadoSerializer(source='fk_libro', read_only=True)
    
    class Meta:
        model = Autoria
        fields = ['id', 'autor', 'autor_id', 'libro', 'libro_id', 'libros_escritos']

    def create(self, validated_data):
        # Extraer los IDs de autor y libro desde los datos validados
        autor = validated_data.pop('fk_autor')
        libro = validated_data.pop('fk_libro')
        
        # Crear la nueva instancia de Autoria
        autoria = Autoria.objects.create(fk_autor=autor, fk_libro=libro, **validated_data)
        return autoria
