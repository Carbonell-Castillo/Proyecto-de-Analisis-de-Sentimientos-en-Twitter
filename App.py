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



@app.route('/limpiarDatos', methods=['POST'])
def limpiar():
    pass

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
            procesador.grabar_configuracion(mensaje_xml)
            
            with open("DB/resumenConfigTemp.xml", "r") as xml_file:
                xml_content = xml_file.read()
            
            return xml_content
        else:
            return 'Formato de archivo XML no válido'

    except Exception as e:
        return 'Error al procesar el archivo XML: ' + str(e)

@app.route('/devolverHashtags', methods=['GET'])
def devolverHashtags():
    global fechas_seleccionadas

    if request.method == 'GET':
        fecha_inicial = request.args.get('fecha_inicial')
        fecha_final = request.args.get('fecha_final')

        procesador = ProcesarArchivo(xml_file_path)
        resultado= procesador.consultarHashtags(fecha_inicial, fecha_final)

        return resultado
        
@app.route('/devolverMenciones', methods=['GET'])
def devolverMenciones():
    global fechas_seleccionadas

    if request.method == 'GET':
        fecha_inicial = request.args.get('fecha_inicial')
        fecha_final = request.args.get('fecha_final')

        procesador = ProcesarArchivo(xml_file_path)
        resultado= procesador.consultarMenciones(fecha_inicial, fecha_final)

        return resultado
        





if __name__ == '__main__':
    app.run()
