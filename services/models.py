from django.db import models

# Create your models here.
# Los modelos deben tratarse en singular
#verbose_name=Alias
class Service (models.Model):
    title=models.CharField(max_length=200, verbose_name="Titulo")
    subtitulo= models.CharField(max_length=200, verbose_name="Subtitulo")
    image=models.ImageField(verbose_name="Imagen",upload_to="services")
    content=models.TextField(verbose_name="Contenido")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta: #configuraciones adicionales al modelo
        verbose_name="servicio" #trabaja metadatos
        verbose_name_plural="servicios"
        ordering=['-created'] #['-created'] del ultimo al primero/ ['created'] del primero al ultimo

    def __str__(self):
        return self.title
