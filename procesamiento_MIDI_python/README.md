# Procesador MIDI de Tintinnabulación en Python

Esta herramienta permite tomar un archivo MIDI de entrada con una melodía principal (M-Voice) y generar automáticamente un nuevo archivo MIDI que contiene la voz de acompañamiento (T-Voice) calculada según los parámetros introducidos. El proceso se ejecuta íntegramente en Python.

## Dependencias

* **Python 3.x**.
* **Librería music21** de Python.
## Instalación y Configuración

1. **Instalar music21:** Abre la terminal o línea de comandos y ejecuta:
   `pip install music21`
2. **Preparar los archivos:** Asegúrate de que el script `proc_MIDI_python.py`, el archivo `tintinnabulador.py` y el archivo `.mid` que deseas procesar se encuentren guardados dentro de la misma carpeta.

## Uso Básico

1. Ejecuta el script `proc_MIDI_python.py`
3. La consola irá pidiendo los siguientes parámetros:
   * **Archivo de entrada:** Nombre completo del MIDI original (ej `melodia.mid`).
   * **Nota base:** Nota fundamental de la secuencia soporte (ej. `C`, o escribe `a` para que el script detecte la tonalidad automáticamente).
   * **Intervalos:** Estructura de la secuencia soporte separada por guiones (ej. `0-4-7`).
   * **Nivel Tintinnabuli:** Nivel de la voz que se desea generar (cualquier número entero distinto de `0`).
   * **Archivo de salida:** Nombre del archivo resultante (ej. `resultado.mid`).
4. Al pulsar Enter en el último paso, la herramienta procesará las notas y guardará el nuevo archivo MIDI directamente en esta carpeta.