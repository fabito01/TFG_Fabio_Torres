# Herramienta de Tintinnabulación Estática

Esta herramienta permite seleccionar una melodía MIDI en REAPER y generar automáticamente una pista nueva con la voz de acompañamiento (T-Voice) calculada según los parámetros introducidos. El núcleo matemático se ejecuta en Python, mientras que Lua actúa como puente con la API de ReaScript.

## Dependencias

* **REAPER 7.x** (Compatible con Windows, MacOS y Linux).
* **Python 3.x**.
* **Librería music21** de Python.

## Instalación y Configuración

1. **Instalar music21:** Abre tu terminal o línea de comandos y ejecuta:
   `pip install music21`
2. **Configurar la ruta del script:** Abre el archivo `puente_reaper_python.lua` con un editor de texto. Localiza la variable `script_python` y modifícala para que contenga la ruta donde has guardado el archivo `generador_matriz.py` en tu ordenador.
3. **Integrar en REAPER:** 
   * Abre REAPER y ve a `Actions` -> `Show action list`.
   * Selecciona `New/Load ReaScript` y carga tu archivo `puente_reaper_python.lua`.

## Uso Básico

1. Crea una pista en REAPER y dibuja o graba un ítem MIDI con la melodía principal (M-Voice).
2. Selecciona el ítem MIDI haciendo clic sobre él.
3. Abre la lista de acciones (`Actions` -> `Show action list`) y ejecuta el script `puente_reaper_python.lua`.
4. Aparecerá una ventana emergente pidiendo los parámetros:
   * **Base Note:** Nota base de la secuencia.
   * **Semitones:** Intervalos separados por guiones.
   * **T-Voice:** Nivel de la voz que deseas obtener.
5. Al darle a OK, la herramienta creará una pista nueva al final del proyecto con la voz tintinnabulada calculada.

Para visualizar gráficamente este proceso, se adjunta un pequeño tutorial en el siguiente enlace: https://drive.google.com/drive/folders/1HErMpItq5g7-L8kzCyXdH56GMS1Gh_s5?usp=sharing