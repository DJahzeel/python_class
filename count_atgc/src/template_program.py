'''
NAME: Contador de Nucleótidos
VERSION: 1.0
AUTHOR: Palafox Collaodo Dara Jazheel. darapc@lcg.unam.mx
DESCRIPTION: Este programa cuenta la cantidad de cada nucleótido en una secuencia de DNA e imprime los resultados en pantalla. 
La secuencia viene en un archivo de texto en formato raw llamado sequence.txt. 
CATEGORY: Bioinformática
USAGE:
    % python contador_nucleotidos.py
ARGUMENTS: No requiere argumentos de línea de comandos.
METHOD: El programa abre un archivo de texto con una secuencia de DNA, lee su contenido y cuenta la cantidad de cada nucleótido presente en la secuencia. 
SEE ALSO: No aplica
'''

# ===========================================================================
# =                            imports
# ===========================================================================
# No se requieren importaciones adicionales.

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
# No se requieren opciones de línea de comandos.

# ===========================================================================
# =                            functions
# ===========================================================================
# No se requieren funciones adicionales.

# ===========================================================================
# =                            main
# ===========================================================================
# step 1. Abrir el archivo sequence.txt en modo lectura
with open('sequence.txt', 'r') as file:
    # step 2. Leer el contenido del archivo
    sequence = file.read()

# Inicializar los contadores para cada nucleótido
count_A = 0
count_C = 0
count_G = 0
count_T = 0

# Recorrer la secuencia de DNA y contar cada nucleótido
for nucleotide in sequence:
    if nucleotide == 'A':
        count_A += 1
    elif nucleotide == 'C':
        count_C += 1
    elif nucleotide == 'G':
        count_G += 1
    elif nucleotide == 'T':
        count_T += 1

# Imprimir los resultados de los conteos
print('Contenido de nucleótidos en la secuencia de DNA:')
print(f'A: {count_A}')
print(f'C: {count_C}')
print(f'G: {count_G}')
print(f'T: {count_T}')
