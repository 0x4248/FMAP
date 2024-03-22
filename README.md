# FMAP

A audio file format that takes in frequency values or notes and turns them into WAV format.

## File format

The FMAP file format is a simple text file that contains a list of frequency values or notes and some meta data.

Example:

```
t:FMAP test tune
d:A test of the FMAP file format
l:GNU General public licence v3.0 
v:0.5
r:4
--NOTES--
C4,$3,E4,D4,C4,C4,G4,$3,F4,E4,*2,G4,$3,E4,D4,C4,C4
--END--
```

### Metadata

There are some meta data with the file, these are:

`t` - Title
`d` - Description
`l` - Licence
`v` - Volume
`r` - Rate (Notes per second)
`f` - Fade between notes (To prevent clicking)

### Notes

Notes can be defined by putting in the note as it is `C4` (Middle C). You can also enter frequencies in Hz.

A `$` With a number means the last note played will be repeated again the amount you specify. A `*` means there will be a pause for a set amount. For example `400,$3,*2,200` 400Hz will be played 4 times then there will be a 2 note break then 200Hz will be played.

## Usage

The program requires the FMAP file and a output WAV file. There is also a optional `-p` option that will play the WAV file when the rendering has finished.

```
Usage: python3 -m FMAP [file_name] [output] [options]
    file_name: The name of the file to be read
    output: The name of the file to be written
```

## Requirements

The following modules are required:
- numpy
- simpleaudio

These can be installed using pip

```
pip install numpy simpleaudio
```

## Licence

The project is licenced under the GNU General Public Licence v3.0 please see the [LICENCE](LICENCE) for more information