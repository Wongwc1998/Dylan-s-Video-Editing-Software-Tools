import mido, pyautogui, time
import numpy as np

notes_raw=[]
notes=[]
notes_divided=[]
notes2=[]
bpm=206
beat_length=8


names=['gabe','smoke','smoke','boop']

for name in names:
    
    mid = mido.MidiFile('C:/ytpmv/denise/' + name +'.mid', clip=True)
    for msg in mid.tracks[2]:
        if (msg.bytes()[0] == 144 or msg.bytes()[0] == 128):
            notes_raw.append(msg.time)

    notes_raw.pop(0)
    notes_raw.pop(-1)
    notes_raw.append(64)
    notes_raw.append(56)

    for i in range(0,len(notes_raw)//2):
        notes.append((notes_raw[2*i]+notes_raw[2*i+1]))
        notes_divided.append((notes_raw[2*i]+notes_raw[2*i+1])//beat_length)

    notes2=list(np.rint(np.cumsum(notes)/bpm*15,out=np.zeros(len(notes),int),casting='unsafe'))
    #print(notes_raw)
    #print(notes)
    #print(notes_divided)

    print(notes2)

    for ind, notes in enumerate(notes_divided):
        if (notes % 3)!=0:
            print(str(ind) + ", Cannot Execute PyAutoGui")
            
        

    notes_raw=[]
    notes=[]
    notes_divided=[]
    
