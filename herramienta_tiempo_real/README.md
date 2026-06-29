# Tintinnabulador en Tiempo Real (Plugin JSFX)

Esta herramienta consiste en un plugin MIDI nativo para REAPER que procesa la señal de un controlador MIDI y genera el contrapunto tintinnabular de forma interactiva y sin latencia perceptible.

## Dependencias

* Únicamente requiere **REAPER 7.x**. (Está programado en EEL2, el lenguaje nativo de la DAW, por lo que no requiere instalaciones externas).

## Instalación y Configuración

1. En la ventana principal de REAPER, ve a `Options` -> `Show REAPER resource path in explorer/finder`.
2. Entra en la carpeta `Effects` y copia allí el archivo `tintinnabulador_tiempo_real.js` (o el nombre exacto de tu archivo JSFX).
3. Vuelve a REAPER, abre el explorador de efectos en cualquier pista haciendo clic en `FX` y pulsa la tecla `F5` (o haz clic derecho -> `Scan for new plugins`) para que REAPER detecte la nueva herramienta.

## Uso Básico

1. Crea una pista nueva y activa el botón de grabación (`Record Arm`) para que reciba señal MIDI.
2. Abre la ventana de efectos (`FX`) de la pista y añade el plugin llamado **JS: Tintinnabulador Tiempo Real**.
   * **IMPORTANTE:** Este plugin debe ser siempre el **primero** en la cadena de efectos.
3. A continuación (debajo de este plugin), añade un instrumento virtual (VSTi) para generar el sonido.
4. En la interfaz del plugin JSFX, ajusta los *sliders*:
   * **Nota Base / Intervalos:** Define la secuencia soporte.
   * **T-Voice:** Selecciona el nivel de acompañamiento deseado.
   * **Delay T-Voice:** Se puede añadir un retraso en *quarter notes*.
   * **Mantener voz original:** Permite que suene solo el acompañamiento, o la melodía junto al acompañamiento.
   * **Ajuste velocity T-Voice:** Se puede ajustar la intensidad del ataque de las notas de acompañamiento.
5. Finalmente, toca cualquier melodía y escucha la tintinnabulación en vivo.

Para visualizar gráficamente este proceso, se adjunta un pequeño tutorial en el siguiente enlace: https://drive.google.com/drive/folders/1BbX05cWNs1CphM8I7ddW44bd7rrHxLwR?usp=sharing