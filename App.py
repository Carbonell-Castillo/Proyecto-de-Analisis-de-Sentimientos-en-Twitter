from flask import Flask, request, jsonify
from flask_cors import CORS
from Logic.ProcesarArchivo import ProcesarArchivo
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)

# Ruta al archivo XML
xml_file_path = 'DB/mensajes.xml'
xml_file_path_diccionario = 'DB/diccionario.xml'

@app.route('/grabarMensaje', methods=['POST'])
def grabarMensaje():
    try:
        # Verifica si el archivo mensajes.xml ya existe
        #verifica si el archivo mensajes.xml tiene contenido
        treeXML = ET.parse(xml_file_path)
        rootXML = treeXML.getroot()
        if len(rootXML) == 0:
            # Si no existe, crea un nuevo elemento MENSAJES
            print("No existe el archivo")
            root = ET.Element('MENSAJES')
        else:
            print("Existe el archivo")
            # Si ya existe, carga el archivo XML existente
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

        # Obtén el mensaje del archivo XML que se envía en la solicitud POST
        mensaje_xml = ET.fromstring(request.data)
        # Agrega el mensaje al elemento MENSAJES
        root.append(mensaje_xml)

        # Guarda el árbol XML actualizado en el archivo
        tree = ET.ElementTree(root)
        tree.write(xml_file_path)

        return jsonify({'estado': 'Mensaje grabado correctamente'})
    except Exception as e:
        print(e)
        return jsonify({'estado': 'Error al grabar el mensaje'})



@app.route('/procesar_xml', methods=['POST'])
def procesar_xml():
    try:
        xml_file = request.files['mensajes']

        if xml_file.filename.endswith('.xml'):
            # Lee y procesa el archivo XML
            xml_data = xml_file.read()
            mensaje_xml = ET.fromstring(xml_data)

            procesador = ProcesarArchivo(xml_file_path)

            # Llama al método para procesar el XML
            resultado = procesador.procesar_xml(mensaje_xml)

            return resultado
        else:
            return 'Formato de archivo XML no válido'

    except Exception as e:
        return 'Error al procesar el archivo XML: ' + str(e)



@app.route('/grabarConfiguracion2', methods=['POST'])
def procesar_xml2():
    try:
        xml_file = request.files['mensajes']

        if xml_file.filename.endswith('.xml'):
            # Lee y procesa el archivo XML
            xml_data = xml_file.read()
            mensaje_xml = ET.fromstring(xml_data)

            procesador = ProcesarArchivo(xml_file_path_diccionario)

            # Llama al método para procesar el XML
            resultado = procesador.procesar_xml(mensaje_xml)

            return resultado
        else:
            return 'Formato de archivo XML no válido'

    except Exception as e:
        return 'Error al procesar el archivo XML: ' + str(e)





@app.route('/grabarConfiguracion', methods=['POST'])
def procesar_xml3():
    try:
        xml_file = request.files['diccionario']

        if xml_file.filename.endswith('.xml'):
            # Lee y procesa el archivo XML del diccionario
            xml_data = xml_file.read()
            mensaje_xml = ET.fromstring(xml_data)

            procesador = ProcesarArchivo(xml_file_path_diccionario)

            # Llama al método para procesar el XML
            resultado = procesador.grabar_configuracion(mensaje_xml)
            return resultado
            # treeDiccionario = ET.parse(xml_file_path_diccionario)
            # rootDiccionario = treeDiccionario.getroot()

            # for sentimientos in root:
            #     tipo_sentimientos = sentimientos.tag
            #     for palabra_element in sentimientos.findall('palabra'):
            #         palabra = palabra_element.text

            #         # Verifica si la palabra ya existe en el diccionario antes de agregarla
            #         if palabra not in [palabra.text for palabra in rootDiccionario.find(tipo_sentimientos)]:
            #             nueva_palabra = ET.Element('palabra')
            #             nueva_palabra.text = palabra
            #             rootDiccionario.find(tipo_sentimientos).append(nueva_palabra)

            # # Guarda el árbol XML del diccionario actualizado en el archivo
            # treeDiccionario = ET.ElementTree(rootDiccionario)
            # treeDiccionario.write(xml_file_path_diccionario)

        else:
            return 'Formato de archivo XML no válido'

    except Exception as e:
        return 'Error al procesar el archivo XML: ' + str(e)




if __name__ == '__main__':
    app.run()
