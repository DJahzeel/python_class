
**Casos de prueba**

Este documento describe los casos de prueba para el script de Python desarrollado para contar la cantidad de cada nucleótido en una secuencia de ADN y mostrar los resultados en pantalla.

Los casos de prueba se han diseñado considerando las diferentes funcionalidades del script y las posibles situaciones de error.

El script cuenta con dos métodos principales para procesar la secuencia de ADN: uno que abre el archivo "sequence.txt" en modo lectura y otro que abre un archivo especificado por el usuario.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script esté listo para su uso y pueda manejar diferentes condiciones de entrada y situaciones de error.

A continuación, se presentan los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.

---

**Caso de prueba 1: Prueba con el archivo "sequence.txt" predeterminado**

Este caso de prueba verifica si el programa puede contar correctamente los nucleótidos en la secuencia de ADN del archivo predeterminado "sequence.txt".

**Comando de ejecución:**

```bash
python contador_nucleotidos.py
```

**Resultado esperado:** El programa debería imprimir en pantalla los conteos de los nucleótidos A, C, G y T en la secuencia de ADN del archivo "sequence.txt".

---

**Caso de prueba 2: Prueba con un archivo de secuencia de ADN proporcionado por el usuario**

En este caso de prueba, se proporcionará un archivo de secuencia de ADN específico por el usuario y se verificará si el programa cuenta correctamente los nucleótidos en esa secuencia.

**Comando de ejecución:**

```bash
python contador_nucleotidos.py archivo_secuencia_adn.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla los conteos de los nucleótidos A, C, G y T en la secuencia de ADN del archivo proporcionado por el usuario.

---

**Caso de prueba 3: Prueba con un archivo que no existe**

Este caso de prueba verifica si el programa maneja correctamente la situación en la que se proporciona un nombre de archivo que no existe.

**Comando de ejecución:**

```bash
python contador_nucleotidos.py archivo_que_no_existe.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla un mensaje de error indicando que el archivo especificado no fue encontrado.

---

**Caso de prueba 4: Prueba con un archivo vacío**

En este caso de prueba, se proporcionará un archivo vacío y se verificará si el programa puede manejar adecuadamente esta situación.

**Comando de ejecución:**

```bash
python contador_nucleotidos.py archivo_vacio.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla los conteos de todos los nucleótidos como cero.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Caso de prueba 5: Prueba con nucleótidos específicos proporcionados por el usuario**

En este caso de prueba, se proporcionarán nucleótidos específicos por el usuario como argumento opcional, y se verificará si el programa cuenta correctamente los nucleótidos en la secuencia de ADN y si maneja adecuadamente los nucleótidos no válidos.

**Comando de ejecución:**
```
python contador_nucleotidos.py archivo_secuencia_adn.txt -nucleotidos ATGXYZ

```

**Resultado esperado:** El programa debería imprimir en pantalla los conteos de los nucleótidos A, T y G en la secuencia de ADN del archivo proporcionado por el usuario. Además, debería mostrar un mensaje de advertencia indicando que los nucleótidos X, Y y Z no son válidos y finalizar el programa.
Por supuesto, aquí tienes los casos de prueba adicionales que cubren las nuevas funcionalidades implementadas:

---

**Caso de prueba 6: Prueba de análisis de frecuencia de codones**

Este caso de prueba verifica si el programa puede calcular correctamente la frecuencia de los codones en una secuencia de ADN.

**Datos de entrada:**
Secuencia de ADN con varios codones repetidos.

**Comando de ejecución:**
```
python contador_nucleotidos.py archivo_secuencia_adn.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla la frecuencia de cada codón en la secuencia de ADN proporcionada.

---

**Caso de prueba 7: Prueba de identificación de sitios de restricción**

Este caso de prueba verifica si el programa puede identificar correctamente los sitios de restricción en una secuencia de ADN.

**Datos de entrada:**
Secuencia de ADN que contiene uno o más sitios de restricción conocidos.

**Comando de ejecución:**
```
python contador_nucleotidos.py archivo_secuencia_adn.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla la ubicación de los sitios de restricción encontrados en la secuencia de ADN proporcionada.

---

**Caso de prueba 8: Prueba combinada de análisis de frecuencia de codones e identificación de sitios de restricción**

Este caso de prueba verifica si el programa puede realizar correctamente tanto el análisis de la frecuencia de codones como la identificación de sitios de restricción en una secuencia de ADN que contiene ambos elementos.

**Datos de entrada:**
Secuencia de ADN que contiene tanto codones repetidos como sitios de restricción conocidos.

**Comando de ejecución:**
```
python contador_nucleotidos.py archivo_secuencia_adn.txt
```

**Resultado esperado:** El programa debería imprimir en pantalla la frecuencia de cada codón y la ubicación de los sitios de restricción encontrados en la secuencia de ADN proporcionada.


