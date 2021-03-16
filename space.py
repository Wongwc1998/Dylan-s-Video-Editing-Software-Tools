#this is the main file used to automatically change each syllable to the midi note lengths
import sox, mido, numpy as np

import soundfile as sf
import pyrubberband as pyrb
from scipy.io.wavfile import write

bpm = 140  # song bpm
path = r'C:/ytpmv/glados echo/'  # midi filepath
sourcepath = r'C:/ytpmv/glados echo/norm/'  # filepath
temppath=r'C:/ytpmv/'

lyrics="I'm2 gon2 na2 burn my house down in to an ug gly black I'm gon na run aw way now and nev ver look back I'm2 gon2 na2 burn my house down in to an ug gly black I'm gon na run aw way now and nev ver look back I'm2 gon2 na2 burn my house down in to an ug gly black I'm gon na run aw way now and nev ver look back I'm2 gon2 na2 burn my house down in to an ug gly black I'm gon na run aw way now and nev ver look back I'm2 gon2 na2 burn my house down in and nev ver look back and nev ver look back and nev ver look back back"
lyrics="The clocks stopped tick king for rev ver a go How long have I been up Id don't know Ic can't get ag grip But Ic2 can't2 let go2 There was sn't an ny thing toh hold on toth tho Why can'ti is see Why can'ti is see All thec col lors that you see2 Pleasec can Ib be Pleasec can Ib be Co lor ful and free WHAT THEhe HELL'S GOi ING ON2 CAN2 SOME ONE TELL ME PLEASE WHY2 I'M SWITCH chING FAS TER THAN THE2 CHAN NELS ON3 Tee Vee I'm2 black then I'm3 white No some2 thing2 is2 sn't2 right My e ne my's in vi si ble, Id2 don't2 know2 how2 to fight The3 tre mb ling fear is3 more than2 Ic3 can3 take When I'm4 up2 a2 gainst the4 ec cho in2 the5 mirror ec2 cho2 ahh ahh ahh ahh ahh ahh oh2 ahh ahh ahh ahh oh2 oh2 oh2 oh2 ahh ahh ahh ahh ahh ahh ahh ahh ahh ahh know"
l_list = lyrics.split()
concat_list=[]
concat_string=''
new_array=[]
string2=''
wav_dur_array=[]

max_ratio=4.0
done=-1

length_raw=[96, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 192, 48, 48, 48, 48, 192, 48, 48, 48, 48, 96, 96]
length_raw=[96, 96, 96, 48, 96, 48, 48, 48, 48, 192, 48, 48, 48, 48, 48, 192, 48, 96, 144, 96, 96, 48, 48, 96, 48, 48, 48, 96, 192, 48, 48, 48, 48, 48, 96, 48, 48, 48, 96, 240, 96, 48, 96, 144, 96, 48, 96, 144, 96, 48, 96, 144, 96, 96, 192, 96, 48, 96, 144, 96, 48, 96, 144, 96, 48, 96, 144, 288, 48, 48, 96, 48, 48, 96, 96, 48, 48, 48, 48, 192, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 96, 96, 48, 48, 96, 96, 48, 48, 48, 48, 96, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 144, 48, 48, 96, 96, 96, 48, 48, 48, 48, 96, 144, 48, 48, 48, 48, 144, 48, 48, 48, 48, 48, 192, 96, 96, 48, 48, 48, 48, 48, 48, 96, 48, 48, 48, 48, 72, 72, 72, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 96]
beats = list(np.array(length_raw)/bpm*15/24)
space = [0.0]*1000
# math formula for calculating what frame the note should be in.
# (this line code assumes 24 frames per second)

# append 2 because the loop behaves kinda weird if you don't
space.append(0)

notes = [a+b for a,b in zip(space, beats)]
wav_dur_array=[sox.file_info.duration(sourcepath+i+".wav") for i in l_list]
tempo_ratio=[a/b for a,b in zip(wav_dur_array, notes)]
new_array=[b*max_ratio if a/b > max_ratio else a for a,b in zip(beats, wav_dur_array)]
space=[a-b*max_ratio if a/b > max_ratio else 0.0 for a,b in zip(beats, wav_dur_array)]
#changed append to listcomp cause I'm reading fluent python

for i in range(0,min(len(beats),len(l_list))-1):
    if i > done:
        wav_file=sourcepath+l_list[i]+".wav"
        tfm = sox.Transformer()
        concat_string=temppath+'temp/'+l_list[i]+str(i)+'.wav'
        y, sr = sf.read(wav_file)
        data=pyrb.time_stretch(y, sr, wav_dur_array[i]/new_array[i])
        write(concat_string, sr, data)
        tfm.fade(fade_in_len=0.01,fade_out_len=0.01)
        tfm.pad(start_duration=0.0, end_duration=space[i])
    concat_string2=temppath+'temp2/'+l_list[i]+str(i)+'.wav'
    if i > done:
        tfm.build_file(concat_string, concat_string2)
    concat_list.append(concat_string2)
    
comb = sox.Combiner()
comb.build(input_filepath_list=concat_list,output_filepath=sourcepath+'glad2 test '+str(max_ratio)+'.wav',combine_type='concatenate')
