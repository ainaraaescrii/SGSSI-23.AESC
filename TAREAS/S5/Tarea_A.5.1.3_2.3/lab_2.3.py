import hashlib
import sys

def calcular_sha256(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            sha256 = hashlib.sha256()
            while True:
                datos = archivo.read(65536)  # Lee en bloques de 64 KB
                if not datos:
                    break
                sha256.update(datos)
            return sha256.hexdigest()
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

def verificar_archivos(archivo1, archivo2):
    resumen1 = calcular_sha256(archivo1)

    if resumen1 is None:
        return False

    with open(archivo2, 'r') as archivo2_txt:
        contenido2 = archivo2_txt.read()
    
    return contenido2.startswith(resumen1)

def main():
    if len(sys.argv) != 3:
        print("Uso: python verificador.py archivo1.txt archivo2.txt")
        sys.exit(1)

    archivo1 = sys.argv[1]
    archivo2 = sys.argv[2]

    resultado = verificar_archivos(archivo1, archivo2)

    if resultado:
        print("El archivo 2 cumple con la condición.")
    else:
        print("El archivo 2 no cumple con la condición.")

if __name__ == "__main__":
    main()
