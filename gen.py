
import argparse
import os
from mido import MidiFile
import serial
import time

basinc = 0 
def arr2bas(ar,dur):
		# pad to len 3
	a=list(ar)
	a += [0] * (3 - len(a))
	a = a[0:3]
	n0,n1,n2 = a
	global basinc
	basinc+=10
	if dur==0:
		return ''
	basline = "%s tune %d,%d,%d,%d\n"%(basinc,n0,n1,n2,int(dur*1000))
	return basline


parser = argparse.ArgumentParser()
parser.add_argument("midi")
parser.add_argument('-o','--output', help='output basic script')
parser.add_argument('-p','--serial', help='load to module')
parser.add_argument('-l','--loop', help='loop the music',action='store_true')
parser.add_argument('-b','--baud', help='baudrate', default='19200')

args = parser.parse_args()




if args.output==None:
	args.output=args.midi.split('.')[0] + ".bas"

if os.path.isfile(args.midi)!=True:
	print "File '%s' Does not exist!" % (args.midi)
	exit(-1)

basfile = open(args.output,"w")
if basfile == None:
	print "File '%s' could not be opened for writing" % (args.midi)


midifile = MidiFile(args.midi)


activenotes = []

for m in midifile:
	if not m.is_meta:
		if m.type == "note_on":
			activenotes.append(m.note)
			basfile.write( arr2bas(activenotes,m.time) )
		if m.type == "note_off":
			activenotes.remove(m.note)
			basfile.write( arr2bas(activenotes,m.time) )
		#try:
			#print "%s\t%s"%(time,str(activenotes)) 
		#	if m.time !=0:
		#		print " ]\n[ (%f): %s%d" % (m.time,t,m.note) ,
		#	else:
		#		print "%s%d" % (t,m.note) ,
		#except AttributeError:
		#	pass
if args.loop:
	basfile.write("%d goto 20 \n" % (basinc) )
	
basfile.close()
basfile = open(args.output,"r")
if args.serial:
	print "Run sload on board"
	raw_input("press enter when ready")
	ser = serial.Serial(args.serial,int(args.baud))
	for line in basfile:
		ser.write(line.strip()+"\n")
		time.sleep(0.01)

