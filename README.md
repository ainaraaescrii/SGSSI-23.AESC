# SGSSI-23.AESC
Este documento proporciona una guía paso a paso para descargar, compilar (si es necesario) y ejecutar el código fuente desde un repositorio en Python.

## Requisitos previos

1. **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Git**: Debes tener Git instalado para clonar el repositorio. Puedes descargarlo desde [https://git-scm.com/downloads](https://git-scm.com/downloads).

3. **Entorno Virtual (opcional)**: Se recomienda crear un entorno virtual para aislar las dependencias del proyecto. Puedes instalarlo usando `venv` si estás en Python 3.3 o posterior:
   
   ```bash
   python -m venv venv
   ```

   Y luego activa el entorno virtual:

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

   - En macOS y Linux:
     ```bash
     source venv/bin/activate
     ```

## Pasos para descargar y ejecutar el código fuente

1. **Clonar el repositorio**: Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu máquina:

   ```bash
   git clone https://github.com/ainaraaescrii/SGSSI-23.AESC
   ```

2. **Navegar al directorio del proyecto**: Ve al directorio del proyecto usando el comando `cd`:

   ```bash
   cd SGSSI-23.AESC
   ```

3. **Ejecutar el código fuente**: Ejecuta tu código Python con el comando apropiado. Dependiendo de tu proyecto, esto podría ser:

   ```bash
   python nombre_del_script.py
   ```

   Reemplaza `nombre_del_script.py` con el nombre de tu script Python a ejecutar.

## Ejemplo completo

Supongamos que tienes un repositorio en GitHub llamado "mi-proyecto" con un script principal llamado "main.py". Aquí está cómo descargar, compilar (si necesario) y ejecutar el código fuente:

```bash
# Clonar el repositorio
git clone https://github.com/ainaraaescrii/SGSSI-23.AESC

# Navegar al directorio del proyecto
cd SGSSI-23.AESC

# Opcional: Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En macOS y Linux

# Ejecutar el código fuente
python main.py
```
