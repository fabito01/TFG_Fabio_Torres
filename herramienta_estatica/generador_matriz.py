import sys
import json
from music21 import pitch, note, converter
from tintinnabulador import Tintinnabulador

# Dado la nota base, los intervalos y el nivel de tintinnabulación, genera un diccionario
# que vincula cada nota MIDI con su correspondiente nota tintinnabulada.
def generar_matriz_tintinnabuli(nota_base_str, intervalos_str, nivel, archivo_MIDI = None) -> dict:
    if nota_base_str == 'a':
        score = converter.parse(archivo_MIDI, format='midi', quantizePost=False)
        k = score.analyze('key')
        secuencia_soporte = set([
        (k.pitchFromDegree(1).pitchClass) % 12,
        (k.pitchFromDegree(3).pitchClass) % 12,
        (k.pitchFromDegree(5).pitchClass) % 12
        ])
    else:
        nota_base = pitch.Pitch(nota_base_str)
        intervalos = [int(i) for i in intervalos_str.split('-')]
        secuencia_soporte = set([(nota_base.pitchClass + i) % 12 for i in intervalos])

    motor = Tintinnabulador(secuencia_soporte, nivel)

    matriz = {}
    
    #Precalculamos las 128 notas MIDI posibles
    for midi_val in range(128):
        nota_aux = note.Note()
        nota_aux.pitch.midi = midi_val
        
        t_pitch = motor.calcular_tVoice(nota_aux)
        

        # Clave: Nota original. Valor: Nota tintinnabulada.
        matriz[midi_val] = t_pitch.midi

    return matriz

if __name__ == "__main__":
    # Los argumentos de entrada son : nombre_script, nota_base, intervalos, nivel
    # En caso de que no se pasen 4 argumentos de entrada 
    if len(sys.argv) < 4:
        # Imprimimos un JSON válido con el error para que Lua no crashee intentando parsearlo
        print(json.dumps({"error": "Faltan argumentos. Uso: nota_base intervalos nivel"}))
        sys.exit(1)

    nota_base_str = sys.argv[1]
    intervalos_str = sys.argv[2] 
    nivel = int(sys.argv[3])
    archivo_MIDI = sys.argv[4] if len(sys.argv) > 4 else None
    resultado = generar_matriz_tintinnabuli(nota_base_str, intervalos_str, nivel, archivo_MIDI)
    # Imprimimos el resultado en formato JSON para que pueda ser leído por Lua
    print(json.dumps(resultado))
