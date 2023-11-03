from datetime import datetime

def extraer_fecha(texto):
    # Encuentra la parte del texto que contiene la fecha en el formato dd/mm/yyyy
    import re
    fecha_str = re.search(r'\d{2}/\d{2}/\d{4}', texto)
    
    if fecha_str:
        fecha_str = fecha_str.group()
        # Define el formato esperado de la fecha
        formato = "%d/%m/%Y"

        try:
            fecha = datetime.strptime(fecha_str, formato).date()
            return fecha.strftime("%d/%m/%Y")
        except ValueError:
            return None
    else:
        return None

texto1 = "Guatemala, 16/01/2023 10:30 hrs."
texto2 = "Guatemalaa holaa 16/01/2023 10:30 hrs."

fecha1 = extraer_fecha(texto1)
fecha2 = extraer_fecha(texto2)

if fecha1:
    print("Fecha extraída (Texto 1):", fecha1)
else:
    print("No se pudo extraer la fecha del Texto 1.")

if fecha2:
    print("Fecha extraída (Texto 2):", fecha2)
else:
    print("No se pudo extraer la fecha del Texto 2.")
