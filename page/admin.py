from django.contrib import admin
from .models import Page

# Register your models here.
#configuraciones extendidas administrador- modelo

class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
admin.site.register(Page, PageAdmin)