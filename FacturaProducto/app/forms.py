from django import forms 
from .models import Producto, Cliente, Factura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock')
        label = {'descripcion': 'Producto', 'precio': 'Precio', 'stock': 'Stock'}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion')
        label = {'Ruc': 'ruc', 'Nombre': 'Cliente', 'Direccion': 'direccion'}



