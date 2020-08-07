from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ProductoForm,ClienteForm 
from app.models import Producto, Cliente, Factura
# Create your views here.

def menu(request):
    opciones = {'Producto':'Productos en stock', 'Cliente':'Clientes', 'Factura':'Facturas de ventas','Admin':'Administración','Menu':'Menu principal'}
    return render(request, 'principal.html', opciones)

def producto(request):
    opciones = {'Producto': 'Productos en stock', 'Cliente': 'Clientes', 'Factura':'Facturas de ventas'
    , 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)

def editarproducto(request, id):
    opciones = {'Producto': 'Productos en stock', 'Cliente': 'Clientes', 'Factura':'Facturas de ventas'
    , 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'producto.html', opciones)

def listarProducto(request):
    producto = Producto.objects.all( )
    opciones = {'Menu': 'Menu principal', 'Cliente': 'Clientes', 'Factura':'Facturas de ventas', 
    'productos': producto}
    return render(request, 'listar_producto.html', opciones)


def eliminarProdcuto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarproducto')
    return render(request, 'eliminar_producto.html', {'Producto': Producto})

def cliente(request):
    opciones = {'Producto': 'Productos en stock', 'Cliente': 'Clientes', 'Factura':'Facturas de ventas'
    , 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)

def editarcliente(request, id):
    opciones = {'Producto': 'Productos en stock', 'Cliente': 'Clientes', 'Factura':'Facturas de ventas'
    , 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')

    return render(request, 'cliente.html', opciones)

def listarCliente(request):
    cliente = Cliente.objects.all( )
    opciones = {'Menu': 'Menu principal', 'Producto': 'Productos en stock', 'Factura':'Facturas de ventas', 
    'clientes': cliente}
    return render(request, 'listar_cliente.html', opciones)


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarcliente')
    return render(request, 'eliminar_cliente.html', {'Cliente': cliente})

def listarFactura(request):
    factura = Factura.objects.all( )
    opciones = {'Menu': 'Menu principal', 'Producto': 'Productos en stock', 'Cliente':'Clientes', 
    'facturas': factura}
    return render(request, 'listar_factura.html', opciones)