import numpy as np
import mido

notes_raw = []
length_raw = []
space_raw = []
notes = []
length = []
space = []
clips = []
tempo_ratio=[]
bpm = 135  # song bpm
path = r'C:/ytpmv/unr/'  # filepath
midi = 'tunaktunak'
midi = 'verse2'
midi = 'verse1'
midi = 'verse3'
midi = 'unr'



concat_list=[]
concat_string=''
new_array=[]
string2=''
wav_dur_array=[]

thresh_interval=1.0
thresh_ratio_divide=3.0
thresh_ratio_merge=thresh_ratio_divide
long_interval=7.0



# mido reads midi file from filepath
mid = mido.MidiFile(path+midi+'.mid', clip=True)
for msg in mid.tracks[2]:
    #print(msg.bytes())
    if (msg.bytes()[0] == 128):
        #print(msg.time)
        length_raw.append(msg.time)
    if (msg.bytes()[0] == 144):
        #print(msg.time)
        space_raw.append(msg.time) 
space_raw.pop(0)
length_raw[-1]=96
length_raw.append(96)
space_raw.append(0)
print(length_raw)
print(space_raw)

for i in range(len(length_raw)-3):
    length_raw[i]=length_raw[i]+space_raw[i]


print(length_raw)
