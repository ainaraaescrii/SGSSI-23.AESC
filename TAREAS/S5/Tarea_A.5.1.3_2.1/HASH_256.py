import hashlib

# Nombre del archivo de texto
nombre_archivo = '/Users/ainaraaescrii/Desktop/CUARTO/SGSSI/Tareas/S5/Tarea_A.5.1.3_2.1/SGSSI-23.CB.01.txt'


# Función para calcular el resumen SHA-256 de un archivo
def calcular_sha256(nombre_archivo):
    sha256 = hashlib.sha256()
    with open(nombre_archivo, 'rb') as archivo:
        while True:
            data = archivo.read(65536)  # Lee el archivo en bloques de 64 KB
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# Calcula el resumen SHA-256 del archivo y muestra el resultado
try:
    resumen_sha256 = calcular_sha256(nombre_archivo)
    print(f'Resumen SHA-256 del archivo {nombre_archivo}: {resumen_sha256}')
except FileNotFoundError:
    print(f'El archivo {nombre_archivo} no se encuentra en la ubicación especificada.')
except Exception as e:
    print(f'Error al calcular el resumen SHA-256: {str(e)}')
