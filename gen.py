
import argparse
import os
from mido import MidiFile
import serial

basinc = 0 
def arr2bas(ar,dur):
		# pad to len 3
	a=list(ar)
	a += [0] * (3 - len(a))
	a = a[0:3]
	n0,n1,n2 = a
	global basinc
	basinc+=10
	basline = "%s tune %d,%d,%d,%d\n"%(basinc,n0,n1,n2,int(dur*1000))
	return basline


parser = argparse.ArgumentParser()
parser.add_argument("midi")
parser.add_argument('-o','--output', help='output basic script')
parser.add_argument('-p','--serial', help='load to module')

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
basfile.close()
basfile = open(args.output,"r")
if args.serial:
	print "Run sload on board"
	raw_input("press enter when ready")
	ser = serial.Serial(args.serial,19200)
	for line in basfile:
		ser.write(line.strip()+"\n")
	
