import sox

import moviepy.editor as mp

lyrics="Lamp Oil Rope Bombs You want it It's yours my friend As long as2 you2 have e nough ru pees"
lyrics2="Sor ry Link I can't give cre dit Come back when you're a lit tle mmm Ri cher"

wav_dur_array=[]
l_list=lyrics.split()

wav_dur_array=[0]
wav_dur_array_accum=[0]
accum=0
sourcepath=r"C:/ytpmv/morshu/long/"

source_clip = mp.VideoFileClip(sourcepath+'lamprtx.mp4')  # source clip

for i in range(len(l_list)):
    wav_file=sourcepath+l_list[i]+".wav"
    wav_duration=sox.file_info.duration(wav_file)
    wav_dur_array.append(wav_duration)
    accum=accum+wav_duration
    wav_dur_array_accum.append(accum)

print(wav_dur_array)
print(wav_dur_array_accum)

for i in range(1, len(l_list)+1):
    split_clip=source_clip.subclip(wav_dur_array_accum[i-1], wav_dur_array_accum[i])
    split_clip.write_videofile(sourcepath+'rtxvid/'+l_list[i-1]+'.mp4')


wav_dur_array=[0]
wav_dur_array_accum=[0]
accum=0

l_list=lyrics2.split()

source_clip = mp.VideoFileClip(sourcepath+'creditrtx.mp4')  # source clip

for i in range(len(l_list)):
    wav_file=sourcepath+l_list[i]+".wav"
    print(wav_file)
    wav_duration=sox.file_info.duration(wav_file)
    print(wav_file)
    wav_dur_array.append(wav_duration)
    accum=accum+wav_duration
    wav_dur_array_accum.append(accum)

print(wav_dur_array)
print(wav_dur_array_accum)

for i in range(1, len(l_list)+1):
    split_clip=source_clip.subclip(wav_dur_array_accum[i-1], wav_dur_array_accum[i])
    split_clip.write_videofile(sourcepath+'rtxvid/'+l_list[i-1]+'.mp4')
