import xml.etree.ElementTree as ET
from Ventas.models import Cliente


def cargar_xml(ruta_xml):
    try:
        arbol = ET.parse(ruta_xml)
        raiz = arbol.getroot()

        datos = []
        for elemento in raiz.findall('item'):
            numero = elemento.find('numero').text
            nit = elemento.find('nit').text
            nombre = elemento.find('nombre').text
            direccion = elemento.find('direccion').text

            datos.append(Cliente(numero, nit, nombre, direccion))

        return datos
    except Exception as e:
        print(f"Error al cargar XML: {e}")
        return []

def guardar_xml(ruta_xml, datos):
    try:
        root = ET.Element('root')
        for instancia in datos:
            elemento = ET.Element('item')
            ET.SubElement(elemento, 'numero').text = str(instancia.numero)
            ET.SubElement(elemento, 'nit').text = str(instancia.nit)
            ET.SubElement(elemento, 'nombre').text = str(instancia.nombre)
            ET.SubElement(elemento, 'direccion').text = str(instancia.direccion)
            root.append(elemento)

        tree = ET.ElementTree(root)
        with open(ruta_xml, 'wb') as archivo:
            tree.write(archivo, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error al guardar XML: {e}")

def agregar_datos_xml(ruta_xml, nuevos_datos):
    try:
        # Cargar datos existentes del XML
        datos_existentes = cargar_xml(ruta_xml)

        # Agregar nuevos datos
        nuevos_datos_instancia = Cliente(
            numero=nuevos_datos['numero'],
            nit=nuevos_datos['nit'],
            nombre=nuevos_datos['nombre'],
            direccion=nuevos_datos['direccion']
        )

        datos_existentes.append(nuevos_datos_instancia)

        # Guardar datos actualizados en el XML sin ordenar la lista
        guardar_xml(ruta_xml, datos_existentes)
    except Exception as e:
        print(f"Error al agregar datos al XML: {e}")
        
        

# Nuevas funciones en prueba Pendiente
def eliminar_datos_xml(ruta_xml, numero_a_eliminar):
    try:
        # Cargar datos existentes del XML
        datos_existentes = cargar_xml(ruta_xml)

        # Filtrar los datos para excluir el elemento con el número a eliminar
        datos_filtrados = [instancia for instancia in datos_existentes if instancia.numero != numero_a_eliminar]

        # Guardar los datos filtrados en el XML
        guardar_xml(ruta_xml, datos_filtrados)
    except Exception as e:
        print(f"Error al eliminar datos del XML: {e}")