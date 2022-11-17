from django.db import models
from ckeditor.fields import RichTextField
from importlib.resources import contents

# Create your models here.

class Page(models.Model):
    title=models.CharField(verbose_name="Titulo", max_length=200)
    content=RichTextField(verbose_name="Contenido")
    created=models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion"
        )
    updated=models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualizacion"
        )

    class Meta:
        verbose_name="pagina"
        verbose_name_plural="paginas"
        ordering=['title', 'created']

    def __str__(self):
        return self.title