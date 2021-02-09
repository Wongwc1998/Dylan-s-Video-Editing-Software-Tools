import os, sox

lyrics="Switch on the pow wer line Rem mem ber to put on2 Pro tec tion Lay down your pie ces And let's beg gin Ob ject cre ea tion2 Fill in my da ta pa ra me ters In2 it tiali za tion3 Set up our new world And2 let's2 beg gin the2 Si mu la tion4"

lyrics=lyrics.split()

sourcepath=r"C:/ytpmv/execute/glados/"
destpath=r"C:/ytpmv/execute/gladnorm/"

for i in range(len(lyrics)):
    wav_file=sourcepath+str(lyrics[i])+".wav"
    tfm = sox.Transformer()
    tfm.norm(db_level=-1.0)
    tfm.silence(location=-1, silence_threshold=0.1, min_silence_duration=0.01, buffer_around_silence=False)
    concat_string2=destpath+str(lyrics[i])+'.wav'
    tfm.build_file(wav_file, concat_string2)
    
    