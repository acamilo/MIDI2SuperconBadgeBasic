import time
import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument('-b','--baud', help='baudrate', default='19200')
parser.add_argument('-p','--serial', help='load to module')

args = parser.parse_args()


basfile = open(args.file,"r")
ser = serial.Serial(args.serial,int(args.baud))
raw_input("type 'sload' in basic and press enter on badge.\n then press enter here when ready")
for line in basfile:
    print line.strip()
    ser.write(line.strip()+"\n")
    time.sleep(0.01)

