##Contador de la ocurrencia de nucleótidos de ADN en un archivo

Este script de Python está diseñado para contar la cantidad de cada nucleótido en una secuencia de ADN contenida en un archivo de texto y mostrar los resultados en pantalla.

**Uso**
El script se ejecuta desde la línea de comandos y acepta dos argumentos opcionales:

- <nombre_archivo>: Nombre del archivo que contiene la secuencia de ADN.
- [-nucleotidos <letras>]: Opcional. Lista de nucleótidos para los cuales se mostrará la frecuencia. Si no se especifican nucleótidos, se mostrará la frecuencia de todos los nucleótidos (A, T, G, C).

**Salida**
El script imprimirá en pantalla la cantidad de cada nucleótido ('A', 'T', 'G' y 'C') en la secuencia contenida en el archivo. Por ejemplo:

A: 10
C: 8
G: 6
T: 12

Esto indica que hay 10 nucleótidos 'A', 8 nucleótidos 'C', 6 nucleótidos 'G' y 12 nucleótidos 'T' en la secuencia de ADN.

Control de errores
El script maneja varios casos de error:

- Si el archivo proporcionado no se encuentra, mostrará un mensaje de error indicando que el archivo no fue encontrado.
- Si el archivo está vacío, mostrará un mensaje indicando que el archivo está vacío.
- Si la secuencia de ADN contiene caracteres inválidos que no son letras ATGC, mostrará un mensaje indicando los caracteres inválidos encontrados en la secuencia.

Pruebas
Para probar el script, simplemente ejecútalo desde la línea de comandos proporcionando el nombre del archivo que contiene la secuencia de ADN. Asegúrate de que cuente correctamente la cantidad de cada nucleótido en la secuencia contenida en el archivo.

Metadatos y documentación
El script está diseñado y documentado por Palafox Collaodo Dara Jazheel. Proporciona información detallada sobre su uso, argumentos de línea de comandos y manejo de errores.

Código fuente
El código fuente está disponible en este repositorio.

Términos de uso
Este script está disponible bajo la Licencia Apache. Consulta el archivo LICENSE para obtener más detalles.

Cómo citar
Si utilizas este script en tu trabajo, por favor cita: Palafox Collaodo Dara Jazheel (2024). Contador de la ocurrencia de nucleótidos de ADN en un archivo.

Contacto
Si tienes problemas o preguntas, por favor contacta a Palafox Collaodo Dara Jazheel en darapc@lcg.unam.mx.

