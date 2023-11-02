def procesar_texto(texto):
    menciones_estudiante01 = []
    contador_estudiante01 = 0

    palabras = texto.split()  # Divide el texto en palabras

    for palabra in palabras:
        if palabra.startswith('@'):
            mencion = palabra[1:]  # Elimina el "@" del inicio de la palabra
            menciones_estudiante01.append(mencion)
            contador_estudiante01 += 1

    return menciones_estudiante01, contador_estudiante01

texto = "Bienvenido a USAC @estudiante01 por otro lado @estudiante02, es un gusto feliz que seas parte de esta institucion #bienvenidaUSAC#"

menciones, contador = procesar_texto(texto)

print("Menciones:", menciones)
print("Contador de menciones:", contador)
