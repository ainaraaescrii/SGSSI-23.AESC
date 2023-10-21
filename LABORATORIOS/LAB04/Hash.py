import hashlib

# Función para calcular el resumen SHA-256 de un archivo
def calcular_sha256(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            data = file.read(65536)  # Leer el archivo en bloques de 64 KB
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# Nombre del archivo de entrada
archivo = "SGSSI-23.CB.00.txt"

# Calcular el resumen SHA-256 y mostrarlo
hash_resultado = calcular_sha256(archivo)
print("Resumen SHA-256:", hash_resultado)
