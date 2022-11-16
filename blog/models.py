from django.db import models
from tabnanny import verbose
from django.utils.timezone import now
#importar modelo user
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): #tabla categoria - siempre en singular
    name=models.CharField(max_length=200, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=['-created']
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title=models.CharField(max_length=200, verbose_name="Titulo")
    image=models.ImageField(verbose_name="Imagen", upload_to="blog")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(
        verbose_name="Fecha de publicacion", default=now
    )
    author=models.ForeignKey(User, verbose_name="Autor",on_delete=models.CASCADE )#borrar en cascada todo lo referente al autor
    categories=models.ManyToManyField(
        Category, verbose_name="Categorias", related_name="getBlogs"
    )
    created=models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion"
        )
    updated=models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualizacion"
        )

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']
    
    def __str__(self):
        return self.title