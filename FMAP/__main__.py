# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

import sys
import simpleaudio as sa
from FMAP import file, audio

if __name__ == '__main__':
    play = False
    for i in sys.argv:
        if i == "--help":
            print("Usage: python3 -m FMAP [file_name] [output] [options]")
            print("\tfile_name: The name of the file to be read")
            print("\toutput: The name of the file to be written")
            sys.exit()
        if i == "-p":
            play = True    

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print("Computing frequencies")
        notes, title, description, license, note_duration, notes_per_second, volume, sample_rate, fade_between_notes = file.file_to_notes(file_name)

        output = sys.argv[2]
        print("Rendering audio")
        audio.render_audio(output, notes, note_duration, sample_rate, fade_between_notes)
    
        if play:
            print("Playing audio")
            wave_obj = sa.WaveObject.from_wave_file(output)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            print("Finished playing")
        else:
            print("Done")

    else:
        file_name = input("Enter the name of the file: ")
        print("Computing frequencies")
        notes, title, description, license, note_duration, notes_per_second, volume, sample_rate, fade_between_notes = file.file_to_notes(file_name)

        output = input("Enter the name of the output file: ")
        print("Rendering audio")
        audio.render_audio(output, notes, note_duration, sample_rate, fade_between_notes)

        play = input("Do you want to play the audio? (y/n): ")
        if play == "y":
            print("Playing audio")
            wave_obj = sa.WaveObject.from_wave_file(output)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            print("Finished playing")
        else:
            print("Done")