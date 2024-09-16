from django.db import models

# Create your models here.
class Autores(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'autores'

class Libros(models.Model):
    titulo = models.CharField(max_length=255)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'
        
class Autoria(models.Model):
    fk_autor = models.ForeignKey(Autores, models.DO_NOTHING, db_column='fk_autor', related_name='obras')
    fk_libro = models.ForeignKey(Libros, models.DO_NOTHING, db_column='fk_libro', related_name='escritores')
    libros_escritos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autoria'