import unicodedata
import xml.etree.ElementTree as ET
import xml.dom.minidom
from Logic.Analizador import Analizador
from datetime import datetime
import re

class ProcesarArchivo:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    def normalizar_texto(self, texto):
        # Convierte el texto a minúsculas
        texto = texto.lower()

        # Normaliza el texto para eliminar tildes y acentos
        texto_normalizado = ''.join(unicodedata.normalize('NFKD', c) for c in texto)

        # Elimina los caracteres que no son letras
        texto_normalizado = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

        return texto_normalizado

    def procesar_xml(self, mensaje_xml):
        try:
            treeXML = ET.parse(self.xml_file_path)
            rootXML = treeXML.getroot()
            root = mensaje_xml
            
            if len(rootXML) == 0:
                # Si no existe, crea un nuevo elemento MENSAJES
                print("No existen")
                root = ET.Element('MENSAJES')
            else:
                for mensaje in root:
                    # Normaliza el contenido del mensaje (convertir a minúsculas y quitar tildes)
                    texto_fecha = mensaje.find('FECHA').text
                    texto_mensaje = mensaje.find('TEXTO').text
                    analizador = Analizador(texto_fecha, texto_mensaje)
                    analizador.analizar_texto()
                    analizador.generarArchivo()
                    print(texto_mensaje)
                    texto_normalizado = self.normalizar_texto(texto_mensaje)
                    
                    print("Texto normalizado")
                    print(texto_normalizado)
                    mensaje.find('TEXTO').text = texto_normalizado
                    rootXML.append(mensaje)
                

            # Agrega el mensaje XML al elemento MENSAJES
            

            # Guarda el árbol XML actualizado en el archivo
            tree = ET.ElementTree(rootXML)
            tree.write(self.xml_file_path)

            return 'Archivo XML procesado correctamente'
        except Exception as e:
            return 'Error al procesar el archivo XML: ' + str(e)

    def grabar_configuracion(self, configuracion_xml):
        try:
            treeDiccionario = ET.parse(self.xml_file_path)
            rootDiccionario = treeDiccionario.getroot()
            root = configuracion_xml

            palabras_positivas = [palabra.text for palabra in rootDiccionario.find('sentimientos_positivos')]
            palabras_negativas = [palabra.text for palabra in rootDiccionario.find('sentimientos_negativos')]
            palabras_negativas_rechasadas = [palabra.text for palabra in rootDiccionario.find('sentimientos_negativos_rechazados')]
            palabras_positivas_rechasadas = [palabra.text for palabra in rootDiccionario.find('sentimientos_positivo_rechazados')]
            contador_palabras_positivas=0
            contador_palabras_negativas=0
            for sentimientos in root:
                tipo_sentimientos = sentimientos.tag
                for palabra_element in sentimientos.findall('palabra'):
                    palabra = palabra_element.text
                    # Normaliza el texto
                    palabra = self.normalizar_texto(palabra)

                    # Verifica si la palabra ya existe en el diccionario antes de agregarla
                    if palabra not in [palabra.text for palabra in rootDiccionario.find(tipo_sentimientos)]:
                        nueva_palabra = ET.Element('palabra')
                        nueva_palabra.text = palabra
                        

                        # Verifica si la palabra positiva existe en las negativas y viceversa
                        if tipo_sentimientos == 'sentimientos_positivos' and palabra in palabras_negativas:
                            print("Sentimiento positivo en negativo")
                            sentimientos_rechazados = rootDiccionario.find('sentimientos_positivo_rechazados')
                            nueva_palabra_rechazada = ET.Element('palabra')
                            nueva_palabra_rechazada.text = palabra
                            sentimientos_rechazados.append(nueva_palabra_rechazada)
                            
                        elif tipo_sentimientos == 'sentimientos_negativos' and palabra in palabras_positivas:
                            print("Sentimiento negativo en positivo")
                            sentimientos_rechazados = rootDiccionario.find('sentimientos_negativos_rechazados')
                            nueva_palabra_rechazada = ET.Element('palabra')
                            nueva_palabra_rechazada.text = palabra
                            sentimientos_rechazados.append(nueva_palabra_rechazada)
                        else:
                            rootDiccionario.find(tipo_sentimientos).append(nueva_palabra)
                            if tipo_sentimientos == 'sentimientos_positivos':
                                contador_palabras_positivas+=1
                            elif tipo_sentimientos == 'sentimientos_negativos':
                                contador_palabras_negativas+=1
                
            # Guarda el árbol XML del diccionario actualizado en el archivo
            treeDiccionario = ET.ElementTree(rootDiccionario)
            treeDiccionario.write(self.xml_file_path)
             
             # Contar las palabras en cada categoría
            num_palabras_positivas_rechazadas = len(palabras_positivas_rechasadas)
            num_palabras_negativas_rechazadas = len(palabras_negativas_rechasadas)

            # Crear un nuevo árbol XML para el resumen
            resumen_configuracion = ET.Element('CONFIG_RECIBIDA')
            ET.SubElement(resumen_configuracion, 'PALABRAS_POSITIVAS').text = str(contador_palabras_positivas)
            ET.SubElement(resumen_configuracion, 'PALABRAS_POSITIVAS_RECHAZADA').text = str(num_palabras_positivas_rechazadas)
            ET.SubElement(resumen_configuracion, 'PALABRAS_NEGATIVAS').text = str(contador_palabras_negativas)
            ET.SubElement(resumen_configuracion, 'PALABRAS_NEGATIVAS_RECHAZADA').text = str(num_palabras_negativas_rechazadas)

            # Crear el árbol XML y escribirlo en el archivo "resumenConfig.xml"
            resumen_tree = ET.ElementTree(resumen_configuracion)
            xml_string = ET.tostring(resumen_configuracion, encoding='utf-8').decode()
            xml_string = xml.dom.minidom.parseString(xml_string).toprettyxml()
            with open('DB/resumenConfigTemp.xml', 'w') as xml_file:
                xml_file.write(xml_string)

            num_palabras_positivas = len(palabras_positivas)
            num_palabras_negativas = len(palabras_negativas)
            resumen_configuracionTodo = ET.Element('CONFIG_RECIBIDA')
            ET.SubElement(resumen_configuracionTodo, 'PALABRAS_POSITIVAS').text = str(num_palabras_positivas)
            ET.SubElement(resumen_configuracionTodo, 'PALABRAS_POSITIVAS_RECHAZADA').text = str(num_palabras_positivas_rechazadas)
            ET.SubElement(resumen_configuracionTodo, 'PALABRAS_NEGATIVAS').text = str(num_palabras_negativas)
            ET.SubElement(resumen_configuracionTodo, 'PALABRAS_NEGATIVAS_RECHAZADA').text = str(num_palabras_negativas_rechazadas)
            
            with open('DB/resumenConfig.xml', 'w') as xml_file:
                xml_file.write(xml_string)

            return 'Archivo XML procesado correctamente'
        except Exception as e:
            return 'Error al procesar el archivo XML: ' + str(e)

    def consultarSentimientos(self, fechaInicial, fechaFinal):
        with open("DB/mensajes", "r") as xml_file:
            xml_content = xml_file.read()
        resultadoMensaje=""
        for mensaje in xml_content:
            fecha = mensaje.find('FECHA').text
            fecha_str= re.search(r'\d{2}/\d{2}/\d{4}', self.fecha)
            fechaResultado=""

            if fecha_str:
                fecha_str = fecha_str.group()
                formato = "%d/%m/%Y"

                try:
                    fechfechaResultado = datetime.strptime(fecha_str, formato).date()
                    fechaResultado = fecha.strftime("%d/%m/%Y")
                except ValueError:
                    fechaResultado = None
            else:
                fechaResultado = None

            if fechaResultado >= fechaInicial and fechaResultado <= fechaFinal:
                texto = mensaje.find('TEXTO').text
                analizador = Analizador(fecha, texto)
                resultado = analizador.analizarSentimientos(texto)
                resultadoMensaje+= "Fecha: "+ fechaResultado + "\n" + resultado
        return resultadoMensaje
    


                
                
