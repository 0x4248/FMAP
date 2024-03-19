# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

import numpy as np
import wave

def render_audio(output, notes, note_duration, sample_rate):
    output_file = wave.open(output, 'w')
    output_file.setnchannels(1)
    output_file.setsampwidth(2)
    output_file.setframerate(sample_rate)

    max_amplitude = 32767

    for note in notes:
        t = np.linspace(0, note_duration, int(sample_rate * note_duration))
        note_wave = max_amplitude * np.sin(2 * np.pi * note * t)
        note_wave = note_wave.astype(np.int16)
        output_file.writeframes(note_wave.tobytes())

    output_file.close()
