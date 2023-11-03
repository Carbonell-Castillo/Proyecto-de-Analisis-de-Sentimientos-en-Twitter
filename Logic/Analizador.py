from datetime import datetime
import re
import Logic.temp as temp
import Logic.SG as sg
import xml.etree.ElementTree as ET
import xml.dom.minidom

class Analizador:
    def __init__(self, fecha, texto):
        self.fecha = fecha
        self.texto = texto

    def analizar_texto(self):
        ##Analiza las maneciones
        listaMenciones = temp.ListaEnlazada()
        contador = 0

        # Divide el texto en palabras
        palabras = self.texto.split()

        # Recorre todas las palabras del texto
        for palabra in palabras:
            if palabra.startswith('@'):
                if listaMenciones.estaVacia():
                    listaMenciones.agregar(palabra[1:])
                    contador += 1
                else:
                    if not listaMenciones.buscar(palabra[1:]):
                        listaMenciones.agregar(palabra[1:])
                        contador += 1                

        ##buca todos aquellos que tenga #cas#
        listaHashtag = temp.ListaEnlazada()
        contadorHashtag = 0

        for palabra in palabras:
            if palabra.startswith('#') and palabra.endswith('#'):
                if listaHashtag.estaVacia():
                    listaHashtag.agregar(palabra[1:-1])
                    contadorHashtag += 1
                else:
                    if not listaHashtag.buscar(palabra[1: -1]):
                        listaHashtag.agregar(palabra[1: -1])
                        contadorHashtag += 1                

        ##Extrae las fechas
        fecha_str= re.search(r'\d{2}/\d{2}/\d{4}', self.fecha)
        fecha=""
        if fecha_str:
            fecha_str = fecha_str.group()
            formato = "%d/%m/%Y"

            try:
                fecha = datetime.strptime(fecha_str, formato).date()
                fecha = fecha.strftime("%d/%m/%Y")
            except ValueError:
                fecha = None
        else:
            fecha = None
        sg.tempMensajes.agregar(fecha, 1, contador, contadorHashtag)
        print("Se agrego")

    def generarArchivo(self):
        print("Entroo generar archivo")
        sg.tempMensajes.generarArchivo()
        # mensajes_recibidos = ET.Element("MENSAJES_RECIBIDOS")

        # for mensaje in sg.tempMensajes:
        #     tiempo = ET.SubElement(mensajes_recibidos, "TIEMPO")

        #     fecha_element = ET.SubElement(tiempo, "FECHA")
        #     fecha_element.text = mensaje.fecha

        #     msj_recibidos_element = ET.SubElement(tiempo, "MSJ_RECIBIDOS")
        #     msj_recibidos_element.text = str(mensaje.mensajesRecibidos)

        #     usr_mencionados_element = ET.SubElement(tiempo, "USR_MENCIONADOS")
        #     usr_mencionados_element.text = str(mensaje.usuariosMencionados)

        #     hashtags_element = ET.SubElement(tiempo, "HASH_INCLUIDOS")
        #     hashtags_element.text = str(mensaje.hashtags)
        
        # tree = ET.ElementTree(mensajes_recibidos)

        # #guardar el archivo
        # tree.write("DB/resumenMensajesTemp.xml")


    def formatearArchivo(path):
        with open(path, "r") as xml_file:
            xml_content = xml_file.read()

        dom = xml.dom.minidom.parseString(xml_content)
        pretty_xml = dom.toprettyxml(indent="  ")

        # Guardar el archivo XML formateado
        with open(path, "w") as xml_file:
            xml_file.write(pretty_xml)
    