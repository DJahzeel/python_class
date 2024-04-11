**Título del Proyecto:** Contador de Nucleótidos

**Fecha:** 11/04/2024

**Participantes / Autor:** Palafox Collaodo Dara Jazheel (darapc@lcg.unam.mx)

**Descripción del Problema:** El programa tiene como objetivo contar la cantidad de cada nucleótido presente en una secuencia de ADN proporcionada por el usuario. Esta secuencia puede estar contenida en un archivo de texto con formato raw llamado 'sequence.txt' por defecto, o en un archivo especificado por el usuario. 

**Especificación de Requisitos:**

**Requisitos funcionales:**
- El programa debe ser capaz de abrir un archivo de texto que contenga una secuencia de ADN, pudiendo ser 'sequence.txt' por defecto o cualquier archivo especificado por el usuario.
- Se debe leer el contenido del archivo de secuencia de ADN.
- El programa debe realizar el conteo de la cantidad de cada nucleótido ('A', 'C', 'G', 'T') presente en la secuencia.
- Los resultados de los conteos deben ser mostrados de forma clara en pantalla.

**Requisitos no funcionales:**
- El programa se implementará en el lenguaje de programación Python para garantizar una amplia compatibilidad y facilidad de uso.
- Para la lectura de argumentos de línea de comandos, se utilizará la biblioteca argparse de Python, asegurando interfaces de línea de comandos flexibles y amigables para el usuario.
- Se seguirán los estándares de estilo PEP8 para el código Python, lo que mejorará la legibilidad y mantenibilidad del mismo.
- Se prestará especial atención al manejo elegante de errores, proporcionando mensajes claros y significativos para problemas potenciales como rutas de archivos incorrectas o contenido de archivo inválido.
- Se priorizará la eficiencia de la implementación, dado que los archivos de secuencia de ADN pueden ser extensos y requerir procesamiento significativo. Por ende, el programa se diseñará para manejar archivos de entrada grandes de manera eficiente.

**Análisis y Diseño:** El programa se basa en un enfoque simple pero efectivo. Abrirá el archivo 'sequence.txt' por defecto o uno especificado por el usuario. Luego, leerá su contenido y contará la cantidad de cada nucleótido presente en la secuencia de ADN. Finalmente, mostrará los resultados de los conteos en pantalla.

**Pseudocódigo:**
1. Abrir el archivo 'sequence.txt' en modo lectura.
2. Leer el contenido del archivo.
3. Inicializar contadores para cada nucleótido.
4. Recorrer la secuencia de ADN y contar cada nucleótido.
5. Mostrar los resultados de los conteos en pantalla.
6. Solicitar al usuario el nombre del archivo que contiene la secuencia de ADN.
7. Abrir el archivo especificado por el usuario en modo lectura.
8. Leer el contenido del archivo.
9. Inicializar contadores para cada nucleótido.
10. Recorrer la secuencia de ADN y contar cada nucleótido.
11. Mostrar los resultados de los conteos en pantalla.
12. Manejar excepciones para archivos no encontrados.

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
- El programa abre el archivo 'sequence.txt' por defecto o uno especificado por el usuario.
- Se lee la secuencia de ADN del archivo.
- Se cuentan la cantidad de cada nucleótido presente en la secuencia.
- Se muestran los resultados de los conteos en pantalla.

**Flujos alternativos:**
- Manejo de excepciones para archivos no encontrados.

**Casos especiales en el programa:** No aplica.
