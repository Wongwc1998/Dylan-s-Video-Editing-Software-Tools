import numpy as np
import mido

length_raw = []
space_raw = []
bpm = 140  # song bpm
path = r'C:/ytpmv/glados echo/'  # filepath
midi = 'second'

# mido reads midi file from filepath
mid = mido.MidiFile(path+midi+'.mid', clip=True)
length_raw=[msg.time for msg in mid.tracks[2] if (msg.bytes()[0] == 128)]
space_raw=[msg.time for msg in mid.tracks[2] if (msg.bytes()[0] == 144)]
#first space is space before note, delete it
space_raw.pop(0)
#last note is note of unknown length, change it into some ordinary note
length_raw[-1]=96
#add extra note to the end
length_raw.append(96)
space_raw.append(0)

length_raw=[a+b for a,b in zip(length_raw, space_raw)]

print(length_raw)
