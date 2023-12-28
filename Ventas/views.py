from django.shortcuts import redirect, render
from .utils_Cliente import cargar_xml, guardar_xml, agregar_datos_xml, eliminar_datos_xml
from .utils_Factura import cargar_xml_factura, agregar_datos_xml_factura, eliminar_datos_xml_factura, guardar_xml_factura
from .utils_Producto import cargar_xml_producto, agregar_datos_xml_producto, eliminar_datos_xml_producto, guardar_xml_producto

# Create your views here.
#Vistas del Menu
def inicio(request):
    return render(request, 'paginas/inicio.html')

def informacion(request):
    return render(request, 'paginas/informacion.html')
  
##################################################################################################################################  
   
#Vista de Cliente
def Clientes(request):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Clientes.xml'
    datos = cargar_xml(ruta_xml)
    print(datos)
    return render(request, 'Clientes/cliente.html', {'datos': datos})

def Crear_Clientes(request):
    # Asignar la ruta XML de manera automática (puedes modificar esto según tus necesidades)
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Clientes.xml'

    if request.method == 'POST':
        numero = request.POST.get('numero')
        nit = request.POST.get('nit')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')

        nuevos_datos = {
            'numero': numero,
            'nit': nit,
            'nombre': nombre,
            'direccion': direccion,
        }

        agregar_datos_xml(ruta_xml, nuevos_datos)

        return redirect('Clientes')

    return render(request, 'Clientes/crear.html', {'ruta_xml': ruta_xml})



# Funciones en Prueba
def Editar_Clientes(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Clientes.xml'

    # Cargar datos existentes del XML
    datos = cargar_xml(ruta_xml)

    if request.method == 'POST':
        # Obtener los datos actualizados desde el formulario de edición
        numero_editar = request.POST.get('numero')
        nit = request.POST.get('nit')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')

        # Actualizar los datos en la lista
        for instancia in datos:
            if instancia.numero == numero:
                instancia.numero = numero_editar
                instancia.nit = nit
                instancia.nombre = nombre
                instancia.direccion = direccion

        # Guardar los datos actualizados en el XML
        guardar_xml(ruta_xml, datos)

        return redirect('Clientes')

    # Enviar los datos del libro a la plantilla para mostrarlos en el formulario de edición
    cliente_editar = next((instancia for instancia in datos if instancia.numero == numero), None)
    return render(request, 'Clientes/editar.html', {'ruta_xml': ruta_xml, 'Cliente_editar': cliente_editar})

def Eliminar_Clientes(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Clientes.xml'

    # Eliminar datos del XML
    eliminar_datos_xml(ruta_xml, numero)

    return redirect('Clientes')
   
   
   #################################################################################################################
   
# Vistas Factura 
def Facturas(request):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Facturas.xml'
    datos = cargar_xml_factura(ruta_xml)
    print(datos)
    return render(request, 'Facturas/factura.html', {'datos': datos})
   
def Idear_Facturas(request):
    # Asignar la ruta XML de manera automática (puedes modificar esto según tus necesidades)
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Facturas.xml'

    if request.method == 'POST':
        numero = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        maestro = request.POST.get('maestro')
        detalle = request.POST.get('detalle')

        nuevos_datos = {
            'numero': numero,
            'nombre': nombre,
            'maestro': maestro,
            'detalle': detalle,
        }

        agregar_datos_xml_factura(ruta_xml, nuevos_datos)

        return redirect('Facturas')

    return render(request, 'Facturas/idear.html', {'ruta_xml': ruta_xml})

def Revisar_Facturas(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Facturas.xml'

    # Cargar datos existentes del XML
    datos = cargar_xml_factura(ruta_xml)

    if request.method == 'POST':
        # Obtener los datos actualizados desde el formulario de edición
        numero_editar = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        maestro = request.POST.get('maestro')
        detalle = request.POST.get('detalle')

        # Actualizar los datos en la lista
        for instancia in datos:
            if instancia.numero == numero:
                instancia.numero = numero_editar
                instancia.nombre = nombre
                instancia.maestro = maestro
                instancia.detalle = detalle

        # Guardar los datos actualizados en el XML
        guardar_xml_factura(ruta_xml, datos)

        return redirect('Facturas')
       
        # Enviar los datos del libro a la plantilla para mostrarlos en el formulario de edición
    factura_revisar = next((instancia for instancia in datos if instancia.numero == numero), None)
    return render(request, 'Facturas/revisar.html', {'ruta_xml': ruta_xml, 'Factura_revisar': factura_revisar})
                  

def Quitar_Facturas(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Facturas.xml'

    # Eliminar datos del XML
    eliminar_datos_xml_factura(ruta_xml, numero)

    return redirect('Facturas')

#########################################################################################################################################

# Vista Producto
def Productos(request):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Productos.xml'
    datos = cargar_xml_producto(ruta_xml)
    print(datos)
    return render(request, 'Productos/producto.html', {'datos': datos})

def Fundar_Productos(request):
    # Asignar la ruta XML de manera automática (puedes modificar esto según tus necesidades)
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Productos.xml'

    if request.method == 'POST':
        numero = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        nuevos_datos = {
            'numero': numero,
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'stock': stock,
        }

        agregar_datos_xml_producto(ruta_xml, nuevos_datos)

        return redirect('Productos')

    return render(request, 'Productos/fundar.html', {'ruta_xml': ruta_xml})

def Corregir_Productos(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Productos.xml'

    # Cargar datos existentes del XML
    datos = cargar_xml_producto(ruta_xml)

    if request.method == 'POST':
        # Obtener los datos actualizados desde el formulario de edición
        numero_editar = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        # Actualizar los datos en la lista
        for instancia in datos:
            if instancia.numero == numero:
                instancia.numero = numero_editar
                instancia.nombre = nombre
                instancia.descripcion = descripcion
                instancia.precio = precio
                instancia.stock = stock

        # Guardar los datos actualizados en el XML
        guardar_xml_producto(ruta_xml, datos)

        return redirect('Productos')

    # Enviar los datos del libro a la plantilla para mostrarlos en el formulario de edición
    producto_corregir = next((instancia for instancia in datos if instancia.numero == numero), None)
    return render(request, 'Productos/corregir.html', {'ruta_xml': ruta_xml, 'Producto_corregir': producto_corregir})

def Excluir_Productos(request, numero):
    ruta_xml = 'D:\\Universidad\\Vaqueras IPC 2 Guate\\Lab IPC 2\\Negocio\\Comercio\\Inventario\\Ventas\\Archivo\\Productos.xml'

    # Eliminar datos del XML
    eliminar_datos_xml_producto(ruta_xml, numero)

    return redirect('Productos')