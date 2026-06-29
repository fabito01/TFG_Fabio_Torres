from music21 import pitch, note

class Tintinnabulador:
    # El tintinnabulador toma como entrada la secuencia soporte y el nivel de tintinnabulación.
    def __init__(self, secuencia_soporte: set[int], nivel : int):

        self.secuencia_soporte = secuencia_soporte
        self.nivel = nivel

    # Cacula la nota tintinnabulada a partir de la nota original
    # Devuelve un objeto Pitch que guarda el MIDI de la nota resultante.   
    def calcular_tVoice(self, nota_origen : note.Note) -> pitch.Pitch:
        if self.nivel < 0 :
            direccion = -1
        else:
            direccion = 1
        numero_pasos = abs(self.nivel)
        
        midi_val = nota_origen.pitch.midi # Utilizamos el valor MIDI para trabajar con semitonos de forma precisa
        contador = 0
        
        while contador < numero_pasos:
            midi_val += direccion
            if (midi_val % 12) in self.secuencia_soporte: # Pitch class 
                contador += 1

        t_pitch = pitch.Pitch()
        t_pitch.midi = midi_val
        return t_pitch
    
    