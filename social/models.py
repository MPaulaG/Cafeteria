from django.db import models

# Create your models here.
class Social(models.Model):
    key= models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True) 
    #SlugField --> campo para manejar claves
    #unique= True --> es unico 
    name=models.CharField(verbose_name="Red Social", max_length=100)
    url=models.URLField(verbose_name="Enlace", 
        max_length=200, null=True, blank=True)
    created=models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion"
        )
    updated=models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualizacion"
        )
    
    class Meta:
        verbose_name="red social"
        verbose_name_plural="redes sociales"
        ordering=['name']
    
    def __str__(self):
        return self.name