# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

from FMAP.note_convert import convert_note_to_freq

def file_to_notes(file):
    with open(file, 'r') as file:
        notes_file = file.read().splitlines()
    notes_per_second = 4
    note_duration = 1/notes_per_second
    sample_rate = 44100
    volume = 2
    fade_between_notes = 1000
    notes = []
    title = ""
    description = ""
    license= ""
    
    is_notes = False
    for line in notes_file:
        if line.startswith('t:'):
            title = line[2:]
        elif line.startswith('d:'):
            description = line[2:]
        elif line.startswith('l:'):
            license = line[2:]
        elif line.startswith('v:'):
            volume = float(line[2:])
        elif line.startswith('r:'):
            notes_per_second = int(line[2:])
            note_duration = 1/notes_per_second
        elif line.startswith('f:'):
            fade_between_notes = int(line[2:])
            if fade_between_notes == 0:
                fade_between_notes = 1
        if line == '--NOTES--':
            is_notes = True
            continue
        elif line == '--END--':
            break
        elif is_notes:
            if line[0] == '#':
                continue
            else:
                for line in line.split(','):

                    if line.startswith('C') or line.startswith('D') or line.startswith('E') or line.startswith('F') or line.startswith('G') or line.startswith('A') or line.startswith('B'):
                        notes.append(convert_note_to_freq(line))
                        continue
                    elif line[0] == '$':
                        repeat = int(line[1:])
                        notes.extend(notes[-1] for _ in range(repeat))
                    elif line[0] == '*':
                        mute = int(line[1:])
                        notes.extend(0 for _ in range(mute))
                    else:
                        notes.append(int(line))
        else:
            continue
    return notes, title, description, license, note_duration, notes_per_second, volume, sample_rate, fade_between_notes