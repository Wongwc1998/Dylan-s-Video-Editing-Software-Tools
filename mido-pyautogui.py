import mido, pyautogui, time
import numpy as np

notes_raw=[]
notes=[]
notes_divided=[]
beat_length=8
accum=0
bpm=206
beats=[]

flag = True

names=['boop']

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

    beats=list(np.rint(np.cumsum(notes)/bpm*15,out=np.zeros(len(notes),int),casting='unsafe'))
    #print(notes_raw)
    #print(notes)
    #print(notes_divided)

    
    beats.insert(0,0)

    print(beats)


for number, beat in enumerate(beats):
        accum = beat
        pyautogui.click(1065,668)
        time.sleep(0.2)
        pyautogui.press('backspace')
        
        if (accum < 10):
            pyautogui.press(str(accum%10))
        elif (accum < 24):
            pyautogui.press(str(accum//10))
            pyautogui.press(str(accum%10))
        elif (accum < 240):
            pyautogui.press(str(accum//24))
            pyautogui.press(str(accum%24//10))
            pyautogui.press(str(accum%24%10))
        elif (accum < 2400):
            pyautogui.press(str(accum//24//10))
            pyautogui.press(str(accum//24%10))
            pyautogui.press(str(accum%24//10))
            pyautogui.press(str(accum%24%10))
        else:
            pyautogui.press(str(accum//1440))
            pyautogui.press(str(accum//24//10%6))
            pyautogui.press(str(accum//24%10))
            pyautogui.press(str(accum%24//10))
            pyautogui.press(str(accum%24%10))
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')
        


    notes_raw=[]
    notes=[]
    notes_divided=[]
    accum=0

    
