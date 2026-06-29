# TFG: Herramienta MIDI basada en el Tintinnabuli de Arvo Pärt

**Autor:** Fabio Torres Martínez  
**Titulación:** Grado en Matemáticas (Universidad Complutense de Madrid)

## Descripción del Proyecto

Este repositorio contiene el código fuente desarrollado para mi Trabajo Fin de Grado. El proyecto explora y expande la técnica de composición algorítmica conocida como *tintinnabuli*, creada por el compositor contemporáneo Arvo Pärt. 

Originalmente, esta técnica de contrapunto genera voces de acompañamiento restringidas al acorde tríada de tónica. El objetivo principal de este trabajo es generalizar el algoritmo de Pärt hacia un marco de armonía modal y secuencias de soporte arbitrarias, estudiando su viabilidad estética y técnica.

## Herramientas Desarrolladas

Para llevar este concepto a un entorno de producción musical práctico, se han desarrollado dos aproximaciones integradas en la DAW **REAPER**:

1. **Herramienta Estática:** Utiliza Python y Lua para procesar ítems MIDI ya existentes en el proyecto y generar su correspondiente voz tintinnabulada.
2. **Herramienta en Tiempo Real:** Un plugin JSFX escrito en EEL2 que procesa los eventos MIDI entrantes en el momento, permitiendo tocar el acompañamiento en directo.

En las carpeta código_tfg_fabio_torres se encuentran las instrucciones detalladas de instalación y uso para cada una de las herramientas.
