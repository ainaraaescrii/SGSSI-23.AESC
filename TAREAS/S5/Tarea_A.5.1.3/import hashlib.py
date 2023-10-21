import hashlib
import time

# Función para calcular SHA-256
def calcular_sha256():
    data = b'Hello, World!'  # Datos de ejemplo a los que se aplicará SHA-256
    sha256 = hashlib.sha256()
    sha256.update(data)
    sha256_digest = sha256.hexdigest()

# Número de veces que se ejecutará la función
num_ejecuciones = 1000  # Puedes ajustar este valor según tus necesidades

# Medir el tiempo que lleva ejecutar la función
inicio_tiempo = time.time()

for _ in range(num_ejecuciones):
    calcular_sha256()

fin_tiempo = time.time()

# Calcular el tiempo total y la frecuencia por minuto
tiempo_total = fin_tiempo - inicio_tiempo
frecuencia_por_minuto = num_ejecuciones / tiempo_total * 60

print(f'Se ejecutó la función SHA-256 {num_ejecuciones} veces en {tiempo_total:.2f} segundos.')
print(f'Frecuencia aproximada por minuto: {frecuencia_por_minuto:.2f} ejecuciones por minuto.')
