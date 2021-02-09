import mido, pyautogui, time

notes_raw=[]
notes=[]
notes_divided=[]
beat_length=8
accum=0

flag = True

names=['astro']

for name in names:
    
    mid = mido.MidiFile('C:/ytpmv/astro/' + name +'.mid', clip=True)
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

    #print(notes_raw)
    #print(notes)
    print(notes_divided)

    for ind, notes in enumerate(notes_divided):
        if (notes % 3)!=0:
            print(str(ind)+ " " +str(notes)+ ", Cannot Execute PyAutoGui")
            flag=False

    if flag:
        for beat in notes_divided:
            if (accum < 10):
                print(str(accum%10))
            elif (accum < 24):
                print(str(accum//10)+ ',' +str(accum%10))
            elif (accum < 240):
                print(str(accum//24)+ ',' +str(accum%24//10)+ ',' +str(accum%24%10))
            elif (accum < 2400):
                print(str(accum//24//10)+ ',' +str(accum//24%10)+ ',' +str(accum%24//10)+ ',' +str(accum%24%10))
            else:
                print(str(accum//1440)+ ',' +str(accum//24//10%6)+ ',' +str(accum//24%10)+ ',' +str(accum%24//10)+ ',' +str(accum%24%10))
            accum = accum + beat
        

    notes_raw=[]
    notes=[]
    notes_divided=[]
    accum=0
    flag = True
    
