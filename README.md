# Proyecto 6

## Tabla de contenidos

1. [General Info](#general-info)
2. [Technologías](#technologies)
3. [Instalación](#installation)
4. [Metodología](#collaboration)
5. [Conclusión](#faqs)
### Información general
***
Automatización de pruebas API de Urban.Grocers desde la lista de comprobación para el campo "name".  Las pruebas automatizadas se basan en la lista de comprobación para la creación de un kit de productos y se incluyen 9 pruebas positivas y negativas.

Los test y metodos se dividen en archivos diferentes, esta división ayuda a organizar las pruebas automatizadas y a hacerlas más fáciles de entender y mantener.


## Tecnologías
***
Lista de tecnologías utilizadas en este proyecto:
* [Paycharm](https://example.com): Version 2023.3.2 
* [Pytest](https://example.com): Version 7.1.0
* [Librería Request](https://example.com): Version 1234
## Instalación
***

 
```
$ git clone https://github.com/DamelisQuerales/qa-project-06-es.git
$ cd ../projects/qa-project-06-es
$ npm install
$ npm start
```
Información adicional: se trabajo de manera local con PyCharm
## Contenido
***

> Los cuerpos de la solicitud POST se añadieron en el archivo data.py
> La lista de comprobación completa se encuentra en el archivo create_kit_name_kit_test.py.
> Todas las solicitudes estan almacenadas en el archivo sender_stand_request.py
> La URL y las rutas de solicitud se encuentran en el archivo configuration.py
## Principios
***

1. **Unidad de comprobación:** Para facilitar la identificación de problemas y la corrección de errores, cada prueba se centra en una única funcionalidad o aspecto.
2. **Independencia de datos:** Se utilizan datos que consistentes para las pruebas, para evitar la dependencia de datos específicos.
3. **Autonomía de las pruebas:** Cada prueba debe es capaz de ejecutarse de forma independiente, sin depender del resultado de otras pruebas.


### Conclusión
***
Las pruebas automatizadas de API de Urban.Grocers son una herramienta valiosa que puede ayudar a garantizar que la API funcione correctamente. Con un poco de esfuerzo, puede empezar a automatizar las pruebas de su API de Urban.Grocers.

Códigos de respuesta:
| 200 | 201 | 400 |
