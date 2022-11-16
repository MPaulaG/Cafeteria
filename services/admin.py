from django.contrib import admin
from .models import Service #importar modelo

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
admin.site.register(Service, ServiceAdmin) #se registra el modelo creado
