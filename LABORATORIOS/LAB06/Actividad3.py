import os
import hashlib
import random

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

def actividad_4():
    archivos_validos = {}
    total_zeros = 0

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
            total_zeros += prefijo_zeros

    # Crear una lista de archivos, donde cada archivo aparece un número de veces igual a su número de ceros
    lista_sorteo = [archivo for archivo in archivos_validos for _ in range(archivos_validos[archivo])]

    # Imprimir la lista de sorteo
    print('Lista de sorteo:', lista_sorteo)

    # Seleccionar un archivo al azar de la lista de sorteo
    archivo_seleccionado = random.choice(lista_sorteo)

    print('Archivos válidos:', archivos_validos)
    print('Archivo seleccionado:', archivo_seleccionado)

actividad_4()
