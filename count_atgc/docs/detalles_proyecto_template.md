**Título del Proyecto:** Contador de Nucleótidos

**Fecha:** 11/04/2024

**Participantes / Autor:** Palafox Collaodo Dara Jazheel (darapc@lcg.unam.mx)

**Descripción del Problema:** El programa tiene como objetivo contar la cantidad de cada nucleótido presente en una secuencia de ADN proporcionada por el usuario. El programa debe manejar diferentes situaciones, como archivos vacíos o inexistentes, así como caracteres inválidos en la secuencia de ADN.

**Especificación de Requisitos:**

**Requisitos funcionales:**
- El sistema debe permitir al usuario proporcionar un archivo de entrada que contenga una secuencia de ADN.
- El programa debe contar la frecuencia de cada nucleótido en la secuencia y mostrar los resultados en pantalla.
- Debe ser posible especificar opcionalmente los nucleótidos para los cuales se desea ver la frecuencia.
- El programa debe manejar situaciones como archivos vacíos, archivos no encontrados y caracteres inválidos en la secuencia de ADN y nucleótidos no válidos proporcionados como argumento opcional.

**Requisitos no funcionales:**
- Tiempo de respuesta: El programa debe ejecutarse de manera eficiente incluso con secuencias de ADN largas.
- Seguridad: El programa debe manejar adecuadamente los archivos de entrada para evitar posibles vulnerabilidades.
- Plataforma tecnológica: El programa debe ejecutarse en cualquier sistema operativo compatible con Python.
- Nucleótidos no válidos proporcionados como argumento opcional: Se muestra un mensaje de advertencia indicando los nucleótidos no válidos y se termina el programa.


**Análisis y Diseño:** El programa se basa en un enfoque simple pero efectivo. Abrirá el archivo especificado por el usuario. Luego, leerá su contenido y contará la cantidad de cada nucleótido presente en la secuencia de ADN. Finalmente, mostrará los resultados de los conteos en pantalla.

**Pseudocódigo:**
1. Leer el nombre del archivo de entrada desde la línea de comandos
4. Convertir la secuencia a mayúsculas para uniformidad
5. Recorrer la secuencia de ADN y contar cada nucleótido.
6. Mostrar los resultados de los conteos en pantalla.
13. Manejar excepciones para archivos no encontrados o vacios.

**Formato de los datos de entrada:** Archivo de texto con la secuencia de ADN.

**Caso de uso:**
+---------------+
|   Usuario     |
+-------+-------+
        |
        | 1. Proporciona archivo de entrada
        v
+-----------------+
|                 |
| Contador de    |
| Nucleótidos    |
|                 |
+-----------------+

**Actor:** Usuario que ejecuta el programa.

**Descripción:** El usuario proporciona un archivo de entrada que contiene la secuencia de ADN, y el programa cuenta la cantidad de cada nucleótido presente en la secuencia.

**Flujo principal:**
- El usuario proporciona un archivo de entrada.
- El programa lee la secuencia de ADN desde el archivo.
- Se cuenta la frecuencia de cada nucleótido en la secuencia.
- El programa muestra los resultados de la frecuencia en pantalla.



**Flujos alternativos:**
- Si el archivo proporcionado no se encuentra, se muestra un mensaje de error.
- Si el archivo está vacío, se muestra un mensaje de advertencia.
- Si se encuentran caracteres inválidos en la secuencia, se muestran mensajes de advertencia.


**Casos especiales en el programa:** 
- Archivo no encontrado: Se muestra un mensaje de error.
- Archivo vacío: Se muestra un mensaje de advertencia.
- Caracteres inválidos en la secuencia: Se muestran mensajes de advertencia indicando los caracteres inválidos.
