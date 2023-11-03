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
            procesador.procesar_xml(mensaje_xml)
            
            with open("DB/resumenMensajesTemp.xml", "r") as xml_file:
                xml_content = xml_file.read()
            
            return xml_content

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
            
            with open("DB/resumenConfigTemp.xml", "r") as xml_file:
                xml_content = xml_file.read()
            
            return xml_content
        else:
            return 'Formato de archivo XML no válido'

    except Exception as e:
        return 'Error al procesar el archivo XML: ' + str(e)

@app.route('/devolverHashtags', methods=['POST'])
def devolverHashtags():
    global fechas_seleccionadas

    if request.method == 'POST':
        fecha_inicial = request.form.get('fecha_inicial')
        fecha_final = request.form.get('fecha_final')

        procesador = ProcesarArchivo(xml_file_path)
        resultado= procesador.consultarHashtags(fecha_inicial, fecha_final)

        return resultado
        
@app.route('/devolverMenciones', methods=['POST'])
def devolverMenciones():
    global fechas_seleccionadas

    if request.method == 'POST':
        fecha_inicial = request.form.get('fecha_inicial')
        fecha_final = request.form.get('fecha_final')

        procesador = ProcesarArchivo(xml_file_path)
        resultado= procesador.consultarMenciones(fecha_inicial, fecha_final)

        return resultado
        





if __name__ == '__main__':
    app.run()
