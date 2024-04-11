'''
NAME: Contador de Nucleótidos
VERSION: 1.2
AUTHOR: Palafox Collaodo Dara Jazheel. darapc@lcg.unam.mx
DESCRIPTION: Este programa cuenta la cantidad de cada nucleótido en una secuencia de DNA e imprime los resultados en pantalla. 
    La secuencia viene en un archivo de texto dado por el usuario. 
    El usuario puede especificar opcionalmente los nucleótidos para los cuales desea ver la frecuencia. 
    Si no se especifican nucleótidos, se mostrará la frecuencia de todos los nucleótidos.
    Si el archivo no se encuentra, el programa mostrará el mensaje "Sorry, couldn't find the file".
    Si el archivo está vacío, el programa mostrará el mensaje "Sorry, the file is empty".
    Además, el programa acepta letras ATGC mayúsculas o minúsculas, y cualquier otro carácter que no sea una letra ATGC será considerado inválido.
CATEGORY: Bioinformática
USAGE:
    % python contador_nucleotidos.py <nombre_archivo> [-nucleotidos <letras>]
ARGUMENTS: 
    - <nombre_archivo>: Nombre del archivo que contiene la secuencia de ADN.
    - [-nucleotidos <letras>]: Opcional. Lista de nucleótidos para los cuales se mostrará la frecuencia.
METHOD: 
    El programa abre el archivo de texto especificado por el usuario en modo lectura, 
    lee su contenido y cuenta la cantidad de cada nucleótido presente en la secuencia. 
    Luego, muestra los resultados en pantalla.
SEE ALSO: No aplica
'''
# ===========================================================================
# =                            imports
# ===========================================================================
import sys

# ===========================================================================
# =                            functions
# ===========================================================================
def contar_nucleotidos(filename, nucleotidos=None):
    """
    Cuenta la frecuencia de los nucleótidos en una secuencia de ADN desde un archivo.

    Args:
        filename (str): El nombre del archivo que contiene la secuencia de ADN.
        nucleotidos (set): Opcional. Conjunto de nucleótidos para contar su frecuencia.
                           Si no se especifica, se contarán todos los nucleótidos (A, T, G, C).

    Returns:
        dict: Un diccionario donde las claves son los nucleótidos y los valores son sus frecuencias.

    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
    """
    if nucleotidos is None:
        nucleotidos = {'A', 'T', 'G', 'C'}

    try:
        with open(filename, 'r') as f:
            secuencia = f.read().upper()
if not secuencia:
                print("Sorry, the file is empty.")
                sys.exit(1)

            # Verificar caracteres inválidos
            caracteres_invalidos = set(secuencia) - nucleotidos
            if caracteres_invalidos:
                for caracter in caracteres_invalidos:
                    print(f"Sequence contains {caracter}, it is an invalid character.")
                sys.exit(1)

            conteos = {nucleotido: secuencia.count(nucleotido) for nucleotido in nucleotidos}
            return conteos
    except FileNotFoundError:
        print("Sorry, couldn't find the file.")
        sys.exit(1)

def main():
    """
    Función principal para manejar los argumentos de línea de comandos y contar la frecuencia de nucleótidos.
    """
    if len(sys.argv) < 2:
        print("Uso: python contador_nucleotidos.py <nombre_archivo> [-nucleotidos <letras>]")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    nucleotidos = None

    if '-nucleotidos' in sys.argv:
        indice_args_nucleotidos = sys.argv.index('-nucleotidos') + 1
        nucleotidos = set(sys.argv[indice_args_nucleotidos:])

    conteos = contar_nucleotidos(nombre_archivo, nucleotidos)
    for nucleotido, conteo in conteos.items():
        print(f"{nucleotido}: {conteo}")

if __name__ == "__main__":
    main()
    
