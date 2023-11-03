import xml.etree.ElementTree as ET
import xml.dom.minidom
class Nodo:
    def __init__(self, fecha, mensajesRecibidos, usuariosMencionados, hashtags):
        self.fecha = fecha
        self.mensajesRecibidos = mensajesRecibidos
        self.usuariosMencionados = usuariosMencionados
        self.hashtags = hashtags
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, fecha, mensajesRecibidos, usuariosMencionados, hashtags):
        nuevo_nodo = Nodo(fecha, mensajesRecibidos, usuariosMencionados, hashtags)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    #regresar verdadero si la lista esta vacia
    def estaVacia(self):
        return self.cabeza == None
    
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def generarArchivo(self):
        mensajes_recibidos = ET.Element("MENSAJES_RECIBIDOS")

        actual = self.cabeza
        while actual:
            tiempo = ET.SubElement(mensajes_recibidos, "TIEMPO")
            
            fecha_element = ET.SubElement(tiempo, "FECHA")
            fecha_element.text = actual.fecha

            msj_recibidos_element = ET.SubElement(tiempo, "MSJ_RECIBIDOS")
            msj_recibidos_element.text = str(actual.mensajesRecibidos)

            usr_mencionados_element = ET.SubElement(tiempo, "USR_MENCIONADOS")
            usr_mencionados_element.text = str(actual.usuariosMencionados)

            hashtags_element = ET.SubElement(tiempo, "HASH_INCLUIDOS")
            hashtags_element.text = str(actual.hashtags)
            actual = actual.siguiente
           
        tree = ET.ElementTree(mensajes_recibidos)
        tree.write("DB/resumenMensajesTemp.xml", encoding="utf-8", xml_declaration=True)
        with open("DB/resumenMensajesTemp.xml", "r") as xml_file:
            xml_content = xml_file.read()

        dom = xml.dom.minidom.parseString(xml_content)
        pretty_xml = dom.toprettyxml(indent="  ")

# Guardar el archivo XML formateado
        with open("DB/resumenMensajesTemp.xml", "w") as xml_file:
            xml_file.write(pretty_xml)

# Ejemplo de uso

