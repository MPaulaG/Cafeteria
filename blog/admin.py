from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class BlogAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    #publicar columnas
    list_display= ('title','author', 'published')
    ordering=('author','published')
    #buscador
    search_fields= ('title','content', 'author__username','categories__name')#ojo doble guin bajo

    #navegacion fechas
    date_hierarchy='published'
    
    #añadir filtro
    list_filter= ('author__username','categories__name')

# gestionar desde el administrador
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog,BlogAdmin )