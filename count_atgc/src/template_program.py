'''
NAME: Contador de Nucleótidos
VERSION: 1.1
AUTHOR: Palafox Collaodo Dara Jazheel. darapc@lcg.unam.mx
DESCRIPTION: Este programa cuenta la cantidad de cada nucleótido en una secuencia de DNA e imprime los resultados en pantalla. 
    La secuencia viene en un archivo de texto dado por el usuario. 
    El usuario puede especificar opcionalmente los nucleótidos para los cuales desea ver la frecuencia. 
    Si no se especifican nucleótidos, se mostrará la frecuencia de todos los nucleótidos.
CATEGORY: Bioinformática
USAGE:
    % python contador_nucleotidos.py
ARGUMENTS: No requiere argumentos de línea de comandos.
METHOD: El programa abre el archivo de texto especificado por el usuario en modo lectura, 
    lee su contenido y cuenta la cantidad de cada nucleótido presente en la secuencia. 
    Luego, muestra los resultados en pantalla.
SEE ALSO: No aplica
'''

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
# ===========================================================================
# =                            Command Line Options
# ===========================================================================
parser = argparse.ArgumentParser(description="Contador de Nucleótidos")
parser.add_argument(
    "archivo", help="Nombre del archivo que contiene la secuencia de ADN")
parser.add_argument("nucleotidos", nargs="*", default=[
                    "A", "C", "G", "T"], help="Lista de nucleótidos para los cuales se mostrará la frecuencia")
# ===========================================================================
# =                            functions
# ===========================================================================
# No se requieren funciones adicionales.

# ===========================================================================
# =                            main
# ===========================================================================

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description="Contador de Nucleótidos")
parser.add_argument(
    "archivo", help="Nombre del archivo que contiene la secuencia de ADN")
parser.add_argument("nucleotidos", nargs="*", default=[
                    "A", "C", "G", "T"], help="Lista de nucleótidos para los cuales se mostrará la frecuencia")

try:
    # Parsear los argumentos de línea de comandos
    args = parser.parse_args()

    # Abrir el archivo especificado por el usuario en modo lectura
    with open(args.archivo, 'r') as file:
        # Leer el contenido del archivo
        sequence = file.read()

    # Inicializar los contadores para cada nucleótido
    conteo_nucleotidos = {nucleotido: 0 for nucleotido in args.nucleotidos}

    # Recorrer la secuencia de DNA y contar cada nucleótido
    for nucleotide in sequence:
        if nucleotide in args.nucleotidos:
            conteo_nucleotidos[nucleotide] += 1

    # Imprimir los resultados de los conteos
    print('Contenido de nucleótidos en la secuencia de DNA:')
    for nucleotido, conteo in conteo_nucleotidos.items():
        print(f'{nucleotido}: {conteo}')

except FileNotFoundError:
    print(f"El archivo '{args.archivo}' no fue encontrado.")
