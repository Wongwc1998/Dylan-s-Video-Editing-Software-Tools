import os, sox
from pydub import AudioSegment

lyrics="Lamp Oil Rope Bombs You want it It's yours my friend As long as2 you2 have e nough ru pees"
lyrics2="Sor ry Link I can't give cre dit Come back when you're a lit tle Ri cher"
lyrics2="I can't give cre dit Come back when you're Ri cher"

wav_dur_array=[]
l_list=lyrics.split()
l_list2=lyrics2.split()

print(len(l_list))
print(len(l_list2))

sourcepath=r"C:/ytpmv/morshu/short/"
destpath=r"C:/ytpmv/morshu/short2/"

accum=0

for i in range(len(l_list)):
    wav_file=sourcepath+l_list[i]+".wav"
    wav_duration=sox.file_info.duration(wav_file)*1000
    wav_dur_array.append(wav_duration)
    source_file=sourcepath+"credit short e.wav"
    newAudio = AudioSegment.from_wav(source_file)
    newAudio = newAudio[accum:accum+wav_duration]
    accum=accum+wav_duration
    wav_file_out=destpath+l_list[i]+".wav"
    newAudio.export(wav_file_out, format="wav") #Exports to a wav file in the current path.
