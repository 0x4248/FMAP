# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

C = [16,33,65,131,262,523,1047,2093,4186]
CS = [17,35,69,139,277,554,1109,2217,4435]
D = [18,37,73,147,294,587,1175,2349,4699]
DS = [19,39,78,156,311,622,1245,2489,4978]
E = [21,41,82,165,330,659,1319,2637,5274]
F = [22,44,87,175,349,698,1397,2794,5588]
FS = [23,46,92,185,370,740,1480,2960,5920]
G = [25,49,98,196,392,784,1568,3136,6272]
GS = [26,52,104,208,415,831,1661,3322,6645]
A = [28,55,110,220,440,880,1760,3520,7040]
AS = [29,58,116,233,466,932,1865,3729,7459]
B = [31,62,123,247,494,988,1976,3951,7902]

def convert_note_to_freq(note):
    note = note.upper()
    if '#' in note:
        if 'C' in note:
            return CS[int(note[-1])]
        elif 'D' in note:
            return DS[int(note[-1])]
        elif 'F' in note:
            return FS[int(note[-1])]
        elif 'G' in note:
            return GS[int(note[-1])]
        elif 'A' in note:
            return AS[int(note[-1])]
    else:
        if 'C' in note:
            return C[int(note[-1])]
        elif 'D' in note:
            return D[int(note[-1])]
        elif 'E' in note:
            return E[int(note[-1])]
        elif 'F' in note:
            return F[int(note[-1])]
        elif 'G' in note:
            return G[int(note[-1])]
        elif 'A' in note:
            return A[int(note[-1])]
        elif 'B' in note:
            return B[int(note[-1])]