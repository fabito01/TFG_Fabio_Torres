
from copy import deepcopy
from music21 import converter, note, pitch
from tintinnabulador import Tintinnabulador

#Parámetros de entrada que se piden al usuario

archivo_entrada = input("Introduce el nombre del archivo MIDI de entrada (con extensión .mid): ")
nota_base_str =  input("Introduce la nota base de la secuencia soporte (ej. C,E,G): ")
intervalos_str =  input("Introduce los intervalos de la secuencia soporte (ej. 0-4-7): ")  
nivel_seleccionado = int(input("Introduce el nivel Tintinnabuli a generar: "))
archivo_salida = input("Introduce el nombre del archivo de salida (con extensión .mid): ")

score = converter.parse(archivo_entrada, format='midi', quantizePost=False) 

if nivel_seleccionado == 0:
    raise ValueError("Error: El nivel 0 es la melodía original, no una voz Tintinnabuli.")

if nota_base_str == 'a':
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

#Inicializamos el tintinabulador
tintinnabulador = Tintinnabulador(secuencia_soporte, nivel_seleccionado)

#Parser del archivo MIDI a través de music21
score = converter.parse(archivo_entrada, format='midi',quantizePost=False)
 # El quantizePost es para evitar problemas de timing con los archivos MIDI, aunque no siempre es necesario


score_final = deepcopy(score)
melodia_final = score_final.parts[0]  # Nos vale esto pues nuestro archivo de entrada solo contiene un track
melodia_final.id = "T-Voice"


for n in melodia_final.recurse().notes: # Forma de recorrer solo las notas, ignorando silencios y otros elementos
#Cuidado aquí si nuestra voz tiene acordes. Para eso se mete esta excepcion
    if isinstance(n, note.Note): 
        n.pitch = tintinnabulador.calcular_tVoice(n)

score_final.write('midi', fp=archivo_salida)
print(f"Archivo MIDI generado correctamente: {archivo_salida}")