import os, sox

lyrics="Lamp Oil Rope Bombs You want it It's yours my friend As long as2 you2 have e nough ru pees Lamp2"
lyrics2="Sor ry Link I can't give cre dit Come back when you're a lit tle mmm Ri cher"

lyrics=lyrics.split()
lyrics2=lyrics2.split()

sourcepath=r"C:/ytpmv/morshu/short2/"
destpath=r"C:/ytpmv/morshu/snorm2/"

for i in range(len(lyrics)):
    wav_file=sourcepath+str(lyrics[i])+".wav"
    tfm = sox.Transformer()
    tfm.norm(db_level=-1.0)
    tfm.silence(location=-1, silence_threshold=0.1, min_silence_duration=0.01, buffer_around_silence=False)
    tfm.fade(fade_in_len=0.01,fade_out_len=0.01)
    concat_string2=destpath+str(lyrics[i])+'.wav'
    tfm.build_file(wav_file, concat_string2)
    

for i in range(len(lyrics2)):
    wav_file=sourcepath+str(lyrics2[i])+".wav"
    tfm = sox.Transformer()
    tfm.norm(db_level=-1.0)
    tfm.silence(location=-1, silence_threshold=0.1, min_silence_duration=0.01, buffer_around_silence=False)
    tfm.fade(fade_in_len=0.01,fade_out_len=0.01)
    concat_string2=destpath+str(lyrics2[i])+'.wav'
    tfm.build_file(wav_file, concat_string2)