from .models import Producto, Cliente, Factura
from django.contrib import admin

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('descripcion', 'precio', 'stock', 'creacion')
    ordering = ('descripcion',)
    search_fields = ('descripcion','precio')
    list_filter = ('descripcion',)

class ClineteAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('ruc', 'nombre', 'direccion', 'creacion')
    ordering = ('nombre',)
    search_fields = ('nombre','ruc')
    list_filter = ('nombre',)

class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('cliente', 'fecha','creacion')
    ordering = ('cliente',)
    search_fields = ('cliente',' ')
    list_filter = ('cliente',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClineteAdmin)
admin.site.register(Factura, FacturaAdmin)




