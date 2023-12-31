import hashlib
import time
import re

###############
#### LAB 4 ####
###############

def calcular_sha256(file_path):
    sha256 = hashlib.sha256()

    # Abre el archivo en modo binario para lectura
    with open(file_path, 'rb') as file:
        #Lee el archivo en bloques de 4K para la eficiencia
        for block in iter(lambda: file.read(4096), b""):
            #Actualiza el objeto hash con el bloque actual
            sha256.update(block)

    #Devuelve el resumen SHA-256 en formato hexadecimal
    return sha256.hexdigest()

def agregar_sha256_al_archivo(archivo_entrada, archivo_salida):
    #Lee los contenidos del archivo de entrada
    with open(archivo_entrada, 'r') as input_file:
        contenido_original = input_file.read()

    #Calcula el resumen SHA-256 del archivo de entrada
    resumen_sha256 = calcular_sha256(archivo_entrada)

    #Crea los contenidos para el archivo de salida
    contenido_salida = f"{contenido_original} \nhex: {resumen_sha256}"

    #Escribe los contenidos en el archivo de salida
    with open(archivo_salida, 'w') as output_file:
       output_file.writel(contenido_salida)

def verificar_resumen_en_archivo(archivo_original, archivo_comprobacion):
    # Lee los contenidos del archivo original
    with open(archivo_original, 'r') as original_file:
        contenido_original = original_file.read()

    # Calcula el resumen SHA-256 del archivo original
    resumen_sha256 = calcular_sha256(archivo_original)


    # Lee los contenidos del archivo de comprobación
    with open(archivo_comprobacion, 'r') as comprobacion_file:
        contenido_comprobacion = comprobacion_file.read()

    # Verifica si los contenidos coinciden
    return contenido_comprobacion.startswith(contenido_original) and contenido_comprobacion.strip().endswith(f"hex:{resumen_sha256}")

def calcular_hash_por_min(file):
    start_time = time.time()
    calcular_sha256(file)
    end_time = time.time()
    tiempo_promedio_por_ejecucion = (end_time - start_time)
    ejecuciones_por_minuto = 60 / tiempo_promedio_por_ejecucion if tiempo_promedio_por_ejecucion != 0 else 0

    print(f"Tiempo promedio por ejecución: {tiempo_promedio_por_ejecucion:.6f} segundos")
    print(f"Número aproximado de ejecuciones por minuto: {ejecuciones_por_minuto:.2f}")

#print(calcular_sha256("SGSSI-23.CB.01.txt"))
#calcular_hash_por_min("SGSSI-23.CB.01.txt")

###############
#### LAB 5 ####
###############

def calc_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    return sha256.hexdigest()

def encontrar_proof(contenido_original):
    proof = 0
    while True:
        # Genera la secuencia de 8 caracteres en hexadecimal
        secuencia_hex = format(proof, '08x')

        # Concatena la secuencia de proof al contenido original
        contenido_con_proof = f"{contenido_original}\n{secuencia_hex} 9f 100"

        # Calcula el resumen SHA-256
        resumen_sha256 = calc_sha256(contenido_con_proof)
        
        # Verifica si el resumen comienza con "0"
        if resumen_sha256.startswith("0"):
            print(resumen_sha256)
            return contenido_con_proof

        # Incrementa la proof para la siguiente iteración
        proof += 1

def proof_mas_larga_un_min(contenido_original, tiempo_maximo=60):
    inicio_tiempo = time.time()
    proof = 0
    mejor_hash = ""
    mejor_longitud = 0
    mejor_contenido = 0

    while time.time() - inicio_tiempo < tiempo_maximo:
        secuencia_hex = format(proof, '08x')
        contenido_con_proof = f"{contenido_original}{secuencia_hex}\t9f\t100"
        resumen_sha256 = calc_sha256(contenido_con_proof)

        # Encuentra la longitud de la secuencia de 0s al principio del resumen
        longitud_ceros = len(resumen_sha256) - len(resumen_sha256.lstrip('0'))

        if longitud_ceros > mejor_longitud:
            mejor_longitud = longitud_ceros
            mejor_hash = resumen_sha256
            mejor_contenido = contenido_con_proof

        proof += 1
    
    print(mejor_hash)

    return mejor_contenido

def minar(archivo_entrada, archivo_salida):
    # Lee los contenidos del archivo de entrada
    with open(archivo_entrada, 'r') as input_file:
        contenido_original = input_file.read()

    # Encuentra una secuencia de proof
    contenido_con_proof = proof_mas_larga_un_min(contenido_original)

    # Escribe los contenidos en el archivo de salida
    with open(archivo_salida, 'w') as output_file:
        output_file.write(contenido_con_proof)


def comprobar_condiciones(archivo1, archivo2, ceros):   
    with open(archivo1, 'r') as a1, open(archivo2, 'r') as a2:
        contenido1 = a1.read()
        contenido2 = a2.read()
    ult_fila = contenido2[-15:].split("\t")
    if (contenido2.startswith(contenido1) and len(ult_fila)==3 and re.match(r'^[0-9a-fA-F]{8}$', ult_fila[0]) and 
        re.match(r'^[0-9a-fA-F]{2}$', ult_fila[1]) and ult_fila[2].isdigit()):
        hash_arch2 = calc_sha256(contenido2)
        if hash_arch2.startswith("0"*ceros):
            cond = True
        else:
            cond = False
    else:
        cond = False

    return cond

                          

archivo_entrada = 'SGSSI-23.CB.03.txt'
archivo_salida = 'SGSSI-23.CB.03.9f.txt'
minar(archivo_entrada, archivo_salida)
#print(calc_sha256(archivo_salida))
#print(comprobar_condiciones(archivo_entrada, archivo_salida, 7))


