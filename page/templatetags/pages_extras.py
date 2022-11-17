from page.models import Page
from django import template


#registrar el script como template
register= template.Library()

#agregar un decorador
#decorador es un plus que se da a un metodo 
@register.simple_tag


#consultar todas las paginas secundarias
def get_pages_list():
    pages=Page.objects.all()
    return pages