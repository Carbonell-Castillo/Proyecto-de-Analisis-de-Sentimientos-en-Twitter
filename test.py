import xml.etree.ElementTree as ET

def obtener_textos_en_intervalo(xml_file, fecha_inicio, fecha_fin):
    mensajes = ET.fromstring(xml_file)

    for mensaje in mensajes.findall('MENSAJE'):
        fecha_element = mensaje.find('FECHA').text
        texto = mensaje.find('TEXTO').text

        # Realiza el análisis de la fecha para determinar si está en el intervalo
        fecha = fecha_element.strip()
        if ',' in fecha:
            fecha = fecha.split(',')[1].strip()
        
        # Verifica si la fecha está en el intervalo deseado
        if fecha_inicio <= fecha <= fecha_fin:
            print(fecha_element)
            print(texto)
            print('\n')

# Ejemplo de uso:
xml_file = '''
<MENSAJES>
 <MENSAJE>
   <FECHA>16/01/2023 10:30 hrs.</FECHA>
   <TEXTO>Texto del mensaje 1</TEXTO>
 </MENSAJE>
 <MENSAJE>
   <FECHA>17/01/2023 14:15 hrs.</FECHA>
   <TEXTO>Texto del mensaje 2</TEXTO>
 </MENSAJE>
 <MENSAJE>
   <FECHA>18/01/2023 16:40 hrs.</FECHA>
   <TEXTO>Texto del mensaje 3</TEXTO>
 </MENSAJE>
</MENSAJES>
'''

fecha_inicio = "16/01/2023"
fecha_fin = "18/01/2023"
obtener_textos_en_intervalo(xml_file, fecha_inicio, fecha_fin)
