import hashlib

# Nombre del archivo de entrada y salida
archivo_entrada = "SGSSI-23.CB.02.txt"
archivo_salida = "SGSSI-23.CB.02_modificado.txt"

# Leer el contenido del archivo de entrada
with open(archivo_entrada, 'r') as entrada:
    contenido = entrada.read()

# Generar la secuencia de 8 caracteres en hexadecimal
secuencia_hexadecimal = 'aabbccdd'

# Identificador público del estudiante
identificador_estudiante = '87'

# Crear la línea adicional
linea_adicional = f'{secuencia_hexadecimal}-{identificador_estudiante}-100'

# Crear el archivo de salida y escribir el contenido
with open(archivo_salida, 'w') as salida:
    salida.write(contenido)
    salida.write('\n' + linea_adicional)

# Calcular el resumen SHA-256 del archivo de salida
sha256 = hashlib.sha256()
with open(archivo_salida, 'rb') as archivo:
    while True:
        fragmento = archivo.read(4096)
        if not fragmento:
            break
        sha256.update(fragmento)

# Verificar si el resumen SHA-256 comienza con "0"
resumen = sha256.hexdigest()
if resumen.startswith("0"):
    print(f'Se ha creado el archivo {archivo_salida} con éxito.')
else:
    print(f'El resumen SHA-256 no comienza con "0".')

print(f'Resumen SHA-256: {resumen}')
