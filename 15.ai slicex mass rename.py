#rename each file acquired from 15.ai processed to slicex into their more appropriate names

import os

lyrics="Switch on the pow wer line Rem mem ber to put on2 Pro tec tion Lay down your pie ces And let's beg gin Ob ject cre ea tion2"
lyrics2="Fill in my da ta pa ra me ters In2 it tiali za tion3 Set up our new world And2 let's2 beg2 gin2 the2 Si mu la tion4"
lyrics3="If I can give you all the Si mu la tions Then I2 can2 be your on ly Sa tis fac tion If2 I3 can3 make you2 hap py I4 will run the2 Ex xe cu tion2 Though we are trapped In this strange, strange Si2 mu2 la2 tion3"

lyrics=lyrics.split()
lyrics2=lyrics2.split()
lyrics3=lyrics3.split()
print(len(lyrics3))
route=r"C:/ytpmv/execute/glados/"
for i in range(66):
    try:
        os.rename(route+'glados-1611294001942 - Marker #'+str(i+1)+'.wav', route+lyrics[i]+'.wav')
        os.rename(route+'glados-1611294053288 - Marker #'+str(i+1)+'.wav', route+lyrics2[i]+'.wav')
        os.rename(route+'glados-1611309291544 - Marker #'+str(i+1)+'.wav', route+lyrics3[i]+'.wav')
    except FileNotFoundError:
        continue
