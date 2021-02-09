import os, sox


#lyrics="Ci ty's break king down_2 non_2 a cam mel's back. They just have to go, cause they don't know wack_2 So while you fill the streets, it's ap peal ling to see. You2 won't get out the2 count ty, 'cause you're bad and free. You3 got a2 new hor riz zon, it's2 e phe meral style. A3 mel lan chol ly town where we nev ver smile. And2 all I wan na hear"
#lyrics="feel good"
#lyrics="Laugh ghing gas these haz mats, fast cats. Line ning them up like ass cracks. Play these2 pon nies at2 the track. It's my choc col late att tack. Shit, I'm step ping in the2 heart of this here. Care Bear rap ping2 in2 hard der this2 year. Watch me as I grav vit tate. Yo, we gone ghost town this3 Mo town, With your sound, you in3 the3 blink, Gone2 bite the4 dust, can't fight with2 us, With3 your3 sound,2 you3 kill the5 Inc. So don't stop, get it, get2 it2. Un til you're ched dar head ded. watch2 the6 way I2 nav vig gate. att2"
lyrics="Ci ty's break king down_2 non_2 a cam mel's back. They just have to go, cause they don't know wack_2 So while you fill the streets, it's ap peal ling to see. You2 won't get out the2 count ty, 'cause you're bad and free. You3 got a2 new hor riz zon, it's2 e phe meral style. mel lan chol ly town where we nev ver smile. And2 all I wan na hear is the3 mess sage beep"
lyrics="My dreams, they3 got2 a3 kiss sing. 'Cause2 I2 don't2 get2 sleep, no."
lyrics="Al most Hea ven, West Vir gi nia. Blue Ridge Moun tains, She nan do ah Ri ver. Life is old there, ol der than the trees. Youn ger than2 the2 moun2 tains,2 grow ing like a breeze."
lyrics="Coun try roads take me home To the3 place I be long tin mom ma west hom grow"

lyrics="Wind mill, wind2 mill2 for the3 land. Turn for2 ev ver hand in hand. Take it all2 in2 on your stride. It is tick king, fall ling2 down. Love for3 ev2 ver,2 love3 is3 free ly. Turned for4 ev3 ver3 you4 and3 me. Wind mill, wind2 mill2 for the3 land.2 Is2 ev4 ry bo dy in3"
lyrics="Don't2 stop,2 get it, get it. Peep how your2 cap tain's in4 it.3 Stead dy,"
lyrics="Switch on the pow wer line Rem mem ber to put on2 Pro tec tion Lay down your pie ces And let's beg gin Ob ject cre ea tion2 Fill in my da ta pa ra me ters In2 it tiali za tion3 Set up our new world And2 let's2 beg gin the2 Si mu la tion4"

lyrics=lyrics.split()

sourcepath = r'C:/ytpmv/country/'  # filepath
destpath = r'C:/ytpmv/country/norm/'  # filepath
sourcepath=r"C:/ytpmv/execute/"
destpath=r"C:/ytpmv/execute/gladnorm/"

for i in range(len(lyrics)):
    wav_file=sourcepath+str(lyrics[i])+".wav"
    tfm = sox.Transformer()
    tfm.norm()
    tfm.silence(location=-1, silence_threshold=0.1, min_silence_duration=0.01, buffer_around_silence=False)
    concat_string2=destpath+str(lyrics[i])+'.wav'
    tfm.build_file(wav_file, concat_string2)
    
    