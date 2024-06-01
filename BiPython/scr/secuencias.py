def leer_secuencia(ruta_archivo):
    """
    Lee una secuencia de ADN desde un archivo.

    Args:
    ruta_archivo (str): Ruta del archivo de entrada que contiene la secuencia de ADN.

    Returns:
    str: Secuencia de ADN.
    """
    # Limpiar la ruta de acceso quitando comillas dobles al principio y al final
    ruta_archivo = ruta_archivo.strip('\"')

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            secuencia = ''.join(linea.strip() for linea in lineas if not linea.startswith('>'))
        return secuencia
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}'.")
        return None

def encontrar_codones(marco, secuencia, archivo_salida):
    """
    Encuentra los codones en una secuencia de ADN y los escribe en un archivo de salida.

    Args:
    marco (int): Marco de lectura.
    secuencia (str): Secuencia de ADN.
    archivo_salida (str): Ruta del archivo de salida.
    """
    try:
        with open(archivo_salida, 'w') as archivo:
            if marco < 4:
                inicio = marco - 1
                sec = secuencia[inicio:]
            else:
                inicio = marco - 4 - 1
                sec = complemento_inverso(secuencia)[inicio:]

            codones = [sec[i:i+3] for i in range(0, len(sec), 3) if len(sec[i:i+3]) == 3]
            codones_formateados = ' '.join(codones)

            archivo.write(f'>{archivo_salida}\n')
            archivo.write(codones_formateados)
        print(f'Se generó el archivo {archivo_salida}.')
        return archivo_salida
    except IOError:
        print(f"No se pudo escribir en el archivo '{archivo_salida}'.")
        return None

def complemento_inverso(secuencia):
    """
    Genera el complemento inverso de una secuencia de ADN.

    Args:
    secuencia (str): Secuencia de ADN.

    Returns:
    str: Complemento inverso de la secuencia de ADN de entrada.
    """
    complemento = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complemento[base] for base in reversed(secuencia))

def main():
    """
    Función principal para ejecutar el programa.
    """
    archivo_entrada = input("Por favor, ingrese la ruta del archivo de entrada (seq.nt.fa): ")
    secuencia = leer_secuencia(archivo_entrada)

    if secuencia:
        archivos_generados = []
        for marco in range(1, 7):
            archivo_salida = f'Marco{marco}.fasta'
            resultado = encontrar_codones(marco, secuencia, archivo_salida)
            if resultado:
                archivos_generados.append(resultado)

if __name__ == "__main__":
    main()