# Proyecto de Análisis de Sentimientos en Twitter

## Resumen

El objetivo general de este proyecto es desarrollar una solución integral que implemente tipos de datos abstractos (TDA) y visualización de datos utilizando Graphviz, todo ello bajo el concepto de programación orientada a objetos (POO). Los objetivos específicos incluyen la implementación de POO en Python, el uso de estructuras de programación secuenciales, cíclicas y condicionales, la visualización de TDA's a través de Graphviz y el manejo de archivos XML para la lógica y el comportamiento de la solución.

El proyecto se centra en el desarrollo de una herramienta innovadora para analizar y establecer el sentimiento de los usuarios con respecto a los mensajes publicados en redes sociales, específicamente en Twitter. Esta herramienta se enfoca en la detección de menciones a otros usuarios y hashtags, siendo crucial para determinar si los mensajes contienen sentimientos positivos, negativos o son neutros.

## Palabras clave
Mensajes, programación orientada a objetos, Matrices, Algoritmo de agrupación, Archivos XML.

## Introducción

Este proyecto es el resultado de un esfuerzo dedicado en el ámbito de la analítica de redes sociales.representa una solución integral para la detección y análisis de sentimientos en mensajes de Twitter. Con la creciente importancia de las redes sociales en la sociedad actual, el análisis de sentimientos se ha vuelto fundamental para comprender la percepción de los usuarios y la evolución de las tendencias.

## Desarrollo del Tema

El programa se estructura en dos componentes principales: el Programa 1 (Frontend) y el Servicio 2 (Backend). El frontend proporciona una interfaz web amigable para que los usuarios interactúen con el sistema, mientras que el backend se encarga de cargar, analizar y almacenar datos, así como de generar informes en formato XML.

### Programa 1 - Frontend

El Programa 1 utiliza Django para desarrollar una interfaz de usuario intuitiva. Permite al usuario realizar acciones como cargar archivos de mensajes, cargar archivos de configuración, realizar consultas y generar gráficas. La comunicación con el Servicio 2 se realiza a través de solicitudes HTTP.

### Servicio 2 - Backend

El Servicio 2 utiliza Flask para crear una API RESTful que maneja las solicitudes del Programa 1. Este componente se encarga de cargar archivos XML, procesar datos, generar informes y responder a consultas. Utiliza algoritmos de agrupación y manejo de archivos XML para analizar los sentimientos de los mensajes.

### Tecnologías Clave Utilizadas

- Django: Para el frontend y la interfaz de usuario.
- Flask: Para la creación de la API RESTful del backend.
- XML: Formato de archivo utilizado para almacenar y representar los datos.

## Lectura de Archivos XML

La lectura de datos se realiza mediante archivos XML estructurados que contienen información detallada sobre sistemas y drones. La librería `xml.etree.ElementTree` de Python es esencial para analizar y extraer información de estos archivos.

## Uso de Listas Enlazadas

Se utilizan listas enlazadas para gestionar eficientemente los sistemas y drones. Esto proporciona una estructura dinámica y facilita la manipulación de la información.

## Anexos

Se incluyen detalles sobre la implementación de Flask en el proyecto, la gestión de rutas, el procesamiento de solicitudes y respuestas, y la lectura de archivos XML.

## Conclusiones

El proyecto destaca por el eficaz procesamiento de datos en tiempo real, una interfaz de usuario amigable, flexibilidad y escalabilidad. La herramienta resultante tiene un valor estratégico significativo para comprender la percepción de los usuarios en las redes sociales.

En resumen, este proyecto representa un logro destacado en el desarrollo de una herramienta innovadora para el análisis de datos en redes sociales, con un impacto significativo en la toma de decisiones estratégica.