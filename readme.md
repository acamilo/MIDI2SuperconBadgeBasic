## About
This script will convert a MIDI file into a basic file that you can then play on a badge

## Instalation
You need the mido python midi library
You need argparse
You need pyserial

Just keep pip installing things untill it stops screaming

## Usage
```
python gen.py ~/Downloads/z1overw.mid -o test2.txt -p /dev/ttyUSB0 

usage: gen.py [-h] [-o OUTPUT] [-p SERIAL] midi

positional arguments:
  midi

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output basic script
  -p SERIAL, --serial SERIAL
                        load to module
```
