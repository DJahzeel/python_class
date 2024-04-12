## Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar la frecuencia de los nucleótidos en una secuencia de ADN. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script, así como los posibles errores que puedan surgir.

El script está diseñado para contar la frecuencia de los nucleótidos en una secuencia de ADN y mostrar los resultados en pantalla.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.

**Caso de prueba 1: Comprobación de un archivo de ADN válido**

Descripción: Verificar que el script puede contar la frecuencia de los nucleótidos en una secuencia de ADN válida proporcionada en un archivo.
Datos de entrada: Archivo de texto con una secuencia de ADN válida.
Resultado esperado: El script debe mostrar la frecuencia de cada nucleótido en la secuencia de ADN.
Estado: Éxito

**Caso de prueba 2: Comprobación de un archivo de ADN vacío**

Descripción: Verificar que el script maneje correctamente un archivo de texto que contenga una secuencia de ADN vacía.
Datos de entrada: Archivo de texto vacío.
Resultado esperado: El script debe mostrar un mensaje de error indicando que el archivo está vacío.
Estado: Éxito

**Caso de prueba 3: Comprobación de un archivo de ADN inexistente**

Descripción: Verificar que el script maneje correctamente un archivo de texto que no existe en el sistema.
Datos de entrada: Nombre de archivo inexistente.
Resultado esperado: El script debe mostrar un mensaje de error indicando que no se pudo encontrar el archivo.
Estado: Éxito

**Caso de prueba 4: Comprobación de caracteres inválidos en la secuencia de ADN**

Descripción: Verificar que el script maneje correctamente una secuencia de ADN que contiene caracteres inválidos.
Datos de entrada: Archivo de texto con una secuencia de ADN que contiene caracteres inválidos.
Resultado esperado: El script debe mostrar un mensaje de error indicando los caracteres inválidos encontrados en la secuencia.
Estado: Éxito
