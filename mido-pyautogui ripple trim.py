import mido, pyautogui, time
import numpy as np

notes_raw=[]
notes=[]
beats=[]
beats2=[]

bpm=210 #song bpm
playheadx=1065 #where you playhead is on the screen
playheady=668 #where you playhead is on the screen


mid = mido.MidiFile('C:/ytpmv/unity/oof.mid', clip=True) #mido reads midi file from filepath
for msg in mid.tracks[2]:
    if (msg.bytes()[0] == 144 or msg.bytes()[0] == 128):
        notes_raw.append(msg.time) #mido appends each note to the array

notes_raw.pop(0) #the first note and the last note are irregular so we pop them
notes_raw.pop(-1) #the first note and the last note are irregular so we pop them

for i in range(0,len(notes_raw)//2):
    notes.append((notes_raw[2*i]+notes_raw[2*i+1])) # this loop combines each note and the blank after it into 1 single note.


beats=list(np.rint(np.cumsum(notes)/bpm*15,out=np.zeros(len(notes),int),casting='unsafe'))
beats2=list(np.array(notes)/bpm*15/24)
#math formula for calculating what frame the note should be in.
#(this line code assumes 24 frames per second)
    
beats.insert(0,0) # insert 0 in the 0th element so the loop begins to paste when time is 0.

print(beats) #used for debugging
#print(notes_raw) used for debugging
#print(notes) used for debugging
print(beats2)



for number, beat in enumerate(beats):
    pyautogui.click(playheadx,playheady) # click to change the play head position
    time.sleep(0.1) #waits for a while because Premiere Pro is slow
        
    if (beat < 10):
        pyautogui.press(str(beat%10))
    elif (beat < 24):
        pyautogui.press(str(beat//10))
        pyautogui.press(str(beat%10))
    elif (beat < 240):
        pyautogui.press(str(beat//24))
        pyautogui.press(str(beat%24//10))
        pyautogui.press(str(beat%24%10))
    elif (beat < 2400):
        pyautogui.press(str(beat//24//10))
        pyautogui.press(str(beat//24%10))
        pyautogui.press(str(beat%24//10))
        pyautogui.press(str(beat%24%10))
    else:
        pyautogui.press(str(beat//1440))
        pyautogui.press(str(beat//24//10%6))
        pyautogui.press(str(beat//24%10))
        pyautogui.press(str(beat%24//10))
        pyautogui.press(str(beat%24%10))
    #the whole math equation above masically calculates what buttons to press in Premiere Pro for the time.
    pyautogui.press('enter') # presses enter so Premiere Pro move the playhead
    
    pyautogui.press('w') #ripple trim the video
    pyautogui.hotkey('ctrl', 'v') #pastes the video
    if number % 2 == 0:
        pyautogui.hotkey('alt', 'up') #moves the video up for every second clip
