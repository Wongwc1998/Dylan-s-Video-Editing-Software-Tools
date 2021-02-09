import os

lyrics="Well Sey mour I made it des pite your dir ec tions Ah Su per in tend ent chal mers Wel come hope you're pre pared for an un for2 get ta ble lunch cheon Yeah gah Oh ye gods My roast is ruined what if I3 were to pur chase fast food and dis guise it2 as my2 own cook king ho ho2 ho3 ho4 ho5 Del light ful ly dev vil ish Sey2 mour2 Ah2 Sey3 mour3 Su2 perin tend ent I4 was just stretch ching my3 calves on the win dow sill Ice so met ric ex xer cise Care to2 join me Why is2 there smoke com ing out of your2 ov ven Sey4 mour4 Uh Noooh That isn sn't smoke2 It's steam Steam2 from the2 steamed clams we're hav ving Mmm Steamed2 clams2"
lyrics="Laugh ghing gas these haz mats, fast cats. Line ning them up like ass cracks. Play these2 pon nies at2 the track. It's my choc col late att tack. Shit, I'm step ping in the2 heart of this here."
lyrics="Care Bear rap ping2 in2 hard der this2 year. Watch me as I grav vit tate. Yo, we gone ghost town this3 Mo town, With your sound, you in3 the3 blink, Gone2 bite the4 dust, can't fight with2 us,"
lyrics="With3 your3 sound,2 you3 kill the5 Inc. So don't stop, get it, get2 it2. Un til you're ched dar head ded. watch2 the6 way I2 nav vig gate."
#lyrics="Ci ty's break king a cam mel's back. They just have to go, cause they2 don't know So while you fill the streets, it's ap peal ling to2 see. You2 won't get out the2 count ty, 'cause you're bad and free. You3 got a2 new hor riz zon, it's2 e phe meral style. mel lan chol ly town where we nev ver smile. And2 all I wan na hear is the3 mess sage beep"
lyrics="My dreams, they3 got2 a3 kiss sing. 'Cause2 I2 don't2 get2 sleep, no."
lyrics="Wind mill, wind2 mill2 for the3 land. Turn for2 a ver2 hand in hand. Take it all2 in2 on your stride. It is tick king, fall ling2 down. Love2 for3 ev ver, love3 is3 free ly. Turned for4 ev ver,2 you4 and3 me. Is2 ev2 ry bo dy in3"
# ticking, falling down. Love forever, love is freely. Turned forever, you and me. Is everybody in?"
lyrics="Don't2 stop,2 get it, get it. Peep how your2 cap tain's in4 it.3 Stead dy,"
lyrics="Switch on the pow wer line Rem mem ber to put on2 Pro tec tion Lay down your pie ces And let's beg gin Ob ject cre ea tion2"
lyrics2="Fill in my da ta pa ra me ters In2 it tiali za tion3 Set up our new world And2 let's2 beg2 gin2 the2 Si mu la tion4"
lyrics=lyrics.split()
lyrics2=lyrics2.split()
route=r"C:/ytpmv/execute/"
for i in range(66):
    try:
        os.rename(route+'glados-1611294001942 - Marker #'+str(i+1)+'.wav', route+lyrics[i]+'.wav')
        #os.rename(route+'glados-1611294053288 - Marker #'+str(i+1)+'.wav', route+lyrics2[i]+'.wav')
    except FileNotFoundError:
        continue