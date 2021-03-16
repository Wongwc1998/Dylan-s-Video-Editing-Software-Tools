#this is a wip file that I'll update later when I feel like it, makes movie clips according to midi note length acquired from mido with moviepy

import sys
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
import os
import mido
import pyautogui
import time
import numpy as np
# importing all the packages that we'll use

notes_raw = []
notes = []
beats = []
clips = []
bpm = 150 # song bpmbpm
path = 'C:/ytpmv/morshu/tunak/'  # filepath
sourcepath = r'C:/ytpmv/morshu/long/rtxvid/'  # filepath
midiname = 'pat3'
sourcenames = ['mmm','mmm','mmm']
track_b = [True,True,True,False,False,False,False]

# all this part is setting variables


# mido reads midi file from filepath
mid = mido.MidiFile(path+midiname+'.mid', clip=True)
print(len(mid.tracks))
for track in range(2, len(mid.tracks)):
    if (track_b[track-2] == False):
        continue
    for msg in mid.tracks[track]:
        #print(msg.bytes())
        #print(mido.parse(msg.bytes()))
        #print(mido.Message.from_bytes(msg.bytes()))
        if (len(msg.bytes())>2):
            if (msg.bytes()[0] == 142+track or msg.bytes()[0] == 126+track):
                notes_raw.append(msg.time)  # mido appends each note to the array

    # the first note and the last note are irregular so we pop them
    notes_raw.pop(0)
    notes_raw.pop(-1)

    for i in range(0, len(notes_raw)//2):
        notes.append((notes_raw[2*i]+notes_raw[2*i+1]))
    # this loop combines each note and the blank after it into 1 single note.

    beats = list(np.array(notes)/bpm*15/24)
    # math formula for calculating what frame the note should be in.
    # (this line code assumes 24 frames per second)

    # append 2 because the loop behaves kinda weird if you don't
    beats.append(2)

    #print(notes_raw) #used for debugging
    #print(notes) #used for debugging
    #print(beats) #used for debugging

    source_clip = mp.VideoFileClip(
        sourcepath+sourcenames[track-2]+'.mp4')  # source clip
    test_clip = mp.CompositeVideoClip([source_clip])

    #clips.append(source_clip.subclip(0,item2).fx(vfx.gamma_corr,d_on=0.05, d_off=0.05))
    
    for index, item2 in enumerate(beats):
        if index % 2 == 0:
            clips.append(source_clip.subclip(0, item2))
            #clips.append(test_clip.subclip(0,item2).fx(vfx.blink,d_on=0.05, d_off=0.05))
            # clips.append(source_clip.subclip(0,item2).fx(vfx.gamma_corr,gamma=0.5))
            # clips.append(source_clip.subclip(0,item2).fx(vfx.invert_colors))
            # clips.append(source_clip.subclip(0,item2).fx(vfx.colorx,factor=0.5))
            # clips.append(source_clip.subclip(0,item2).fx(vfx.blackwhite))
            # create a subclip of the source clip and append it to an array
        else:
            clips.append(source_clip.subclip(0, item2))
            # clips.append(source_clip.subclip(0,item2))
            # fx(vfx.mirror_x) flips it
    
    concat_clip = mp.concatenate_videoclips(clips, method="compose")
    # concatenates all of the clips together into one
    concat_clip.write_videofile(sourcenames[track-2]+str(track)+' '+midiname+'.mp4')
    # concatenate every clip and output it
    notes_raw = []
    notes = []
    beats = []
    clips = []
