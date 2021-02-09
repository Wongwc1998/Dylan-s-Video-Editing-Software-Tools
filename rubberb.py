import sox, mido, numpy as np

import soundfile as sf
import pyrubberband as pyrb
from scipy.io.wavfile import write

notes_raw = []
length_raw = []
space_raw = []
notes = []
length = []
space = []
clips = []
tempo_ratio=[]
bpm = 130  # song bpm
path = r'C:/ytpmv/execute/'  # midi filepath
sourcepath = r'C:/ytpmv/execute/gladnorm/'  # filepath
lyrics="Switch on the pow wer line Rem mem ber to put on2 Pro tec tion Lay down your pie ces And let's beg gin Ob ject cre ea tion2 Fill in my da ta pa ra me ters In2 it tiali za tion3 Set up our new world And2 let's2 beg gin the2 Si mu la tion4"
#lyrics=lyrics*3
#lyrics="If I can Ifc Ic canc give you all the Si mu la tions Then I2 can2 Thenc I2c can2c be your on ly Sa tis fac tion If2 I3 can3 make you2 hap py I4 will run the2 Ex xe cu tion2 Though we are trapped In this strange, strange Si2 mu2 la2 tion3"


done=-1


l_list = lyrics.split()
concat_list=[]
concat_string=''
new_array=[]
string2=''
wav_dur_array=[]

thresh_interval=1.0
thresh_ratio_divide=3.0
thresh_ratio_merge=thresh_ratio_divide
long_interval=7.0



length_raw=[96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 72, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 72, 72, 48, 48, 48, 48, 48, 48, 48, 48, 3120, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 96, 96, 96, 48, 96, 48, 48, 96, 48, 48, 144, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 96, 96, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 72, 24, 24, 48, 72, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 96, 96, 48, 96, 48, 48, 96, 48, 48, 48, 96, 96, 96, 48, 96, 48, 48, 96, 48, 48, 144, 96, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 96, 48, 48, 91, 5, 48, 48, 91, 5, 45, 3, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 192, 48, 48, 96, 288, 48, 48, 192, 192, 96, 96, 48, 48, 48, 96]
#length_raw=[96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 96, 48, 48, 96, 48, 48, 96, 96, 48, 48, 48, 96, 96]
space_raw=[0]*500

beats = list(np.array(length_raw)/bpm*15/24)
space = list(np.array(space_raw)/bpm*15/24)
# math formula for calculating what frame the note should be in.
# (this line code assumes 24 frames per second)

#print(beats)

# append 2 because the loop behaves kinda weird if you don't
space.append(0)
#print(len(space))
#print(len(beats))

for i in range (len(beats)):
    notes.append(space[i]+beats[i])

#print(notes)

for i in range(len(l_list)):
    wav_file=sourcepath+l_list[i]+".wav"
    wav_duration=sox.file_info.duration(wav_file)
    wav_dur_array.append(wav_duration)
    
#print(beats)
#print(wav_dur_array)


for i in range(0,min(len(beats),len(wav_dur_array))):
    #print("%5f, %5f" %(notes[i],wav_dur_array[i]))
    tempo_ratio.append(wav_dur_array[i]/notes[i])
#print(tempo_ratio)
    
#beats=divide_this(wav_dur_array, beats, thresh_ratio_divide, long_interval)
#beats=merge_this(wav_dur_array, beats, thresh_ratio_merge)
    
#for i in range(1,99):
    #beats=divide_this(wav_dur_array, beats, thresh_ratio_divide, long_interval)
    
#print(beats)
#print(space)


#print(wav_dur_array)
for i in range(0,min(len(beats),len(l_list))):
    if (beats[i]/wav_dur_array[i])>thresh_ratio_merge:
        space[i]=space[i]+(beats[i]-wav_dur_array[i]*thresh_ratio_merge)
        new_array.append(wav_dur_array[i]*thresh_ratio_merge)
    else:
        new_array.append(beats[i])
    #print(str(i)+' ' + str(new_array[i])+' '+str(space[i]))
    #sum_duration=temp_int
    #print(str(tempo_ratio)+' '+l_list[i]+' '+str(wav_dur_array[i]))
    #tfm = sox.Transformer()
    #tfm.tempo(tempo_ratio)
    #concat_string=sourcepath+'temp/'+str(i)+'.wav'
    #concat_list.append(concat_string)
    #tfm.build(input_filepath=wav_file,output_filepath=concat_string)

#print(concat_list)


#print(beats)
#print(l_list)

#print(new_array)



#print(new_array)
#print(l_list)
#print(space)
for i in range(0,len(space)):
    if space[i]<0.0:
        print("something wrong: " + str(space[i])+' '+l_list[i]+' '+str(wav_dur_array[i])+' '+str(beats[i]))

#print(tempo_ratio)

for i in range(0,min(len(beats),len(l_list))):
    if i > done:
        wav_file=sourcepath+l_list[i]+".wav"
        tfm = sox.Transformer()
        concat_string=sourcepath+'temp/'+l_list[i]+'.wav'
        #print(str(wav_dur_array[i]/new_array[i])+' '+str(new_array[i])+' '+str(wav_dur_array[i])+' ' + str(space[i])+' '+l_list[i])
        y, sr = sf.read(wav_file)
        data=pyrb.time_stretch(y, sr, wav_dur_array[i]/new_array[i])
        write(concat_string, sr, data)
        tfm.fade(fade_in_len=0.01,fade_out_len=0.01)
        tfm.pad(start_duration=0.0, end_duration=space[i])
        #print(wav_dur_array[i], new_array[i], space[i])
    concat_string2=sourcepath+'temp2/'+l_list[i]+str(i)+'.wav'
    if i > done:
        tfm.build_file(concat_string, concat_string2)
    concat_list.append(concat_string2)
    #print(concat_string)
    #print(wav_file)
    
    

#print(concat_list)
comb = sox.Combiner()
comb.build(input_filepath_list=concat_list,output_filepath=sourcepath+'temp/feel good r'+str(thresh_ratio_divide)+'.wav',combine_type='concatenate')
#for i in range(0,len(l_list)):
    #

'''
'''