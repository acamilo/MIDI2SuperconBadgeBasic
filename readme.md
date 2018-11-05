## About
This script will convert a MIDI file into a basic file that you can then play on a badge

## Instalation
You need the mido python midi library
You need argparse
You need pyserial

Just keep pip installing things untill it stops screaming

## Usage
```
python gen.py ~/Downloads/z1overw.mid -o test2.txt -p /dev/ttyUSB0 -l

usage: gen.py [-h] [-o OUTPUT] [-p SERIAL] [-l] midi

positional arguments:
  midi

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output basic script
  -p SERIAL, --serial SERIAL
                        load to module
  -l, --loop            loop the music

```

## Notes
Ok so this thing is kinda hacky.
It'll truncate the maximum notes that can be played at once to 3 which causes some songs to sound wierd..
The loading feature was added because the badge hates Carrage Returns and you need to only send it line feeds.

## Where to find midis
I found some good ones here. https://www.vgmusic.com/music/console/nintendo/gameboy/
