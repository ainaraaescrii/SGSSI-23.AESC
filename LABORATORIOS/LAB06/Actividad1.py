import os
import hashlib

# Ruta del archivo de entrada
archivo_entrada = '/Users/ainaraaescrii/Desktop/CUARTO/SGSSI/LAB06/SGSSI-23.CB.03.txt'

# Ruta de la carpeta local
carpeta_local = '/Users/ainaraaescrii/Desktop/CUARTO/SGSSI/LAB06/SGSSI-23.S.6.2.CB.03.Candidatos'

def calcular_sha256(archivo):
    h = hashlib.sha256()
    with open(archivo, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def verificar_prefijo_zeros(hash):
    return len(hash) - len(hash.lstrip('0'))

def actividad_1():
    archivos_validos = {}
    max_zeros = 0
    archivo_max_zeros = ''

    with open(archivo_entrada, 'r') as file:
        contenido_entrada = file.read()

    for archivo in os.listdir(carpeta_local):
        ruta_archivo = os.path.join(carpeta_local, archivo)
        with open(ruta_archivo, 'r') as file:
            contenido_archivo = file.read()

        if contenido_archivo.startswith(contenido_entrada):
            hash_archivo = calcular_sha256(ruta_archivo)
            prefijo_zeros = verificar_prefijo_zeros(hash_archivo)

            archivos_validos[archivo] = prefijo_zeros

            if prefijo_zeros > max_zeros:
                max_zeros = prefijo_zeros
                archivo_max_zeros = archivo

    print('Archivos válidos:', archivos_validos)
    print('Archivo con más ceros en el prefijo:', archivo_max_zeros)

actividad_1()
