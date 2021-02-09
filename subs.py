#coding=utf-8
from moviepy.video.VideoClip import ImageClip, TextClip
from moviepy.editor import *
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import numpy as np
notes_raw = []
notes = []
beats = []
clips = []
bpm = 138  # song bpm
path = 'C:/ytpmv/morshu/'  # midi filepath
lyrics="na ga re te ku to ki no na ka de de mo,ge da ru sa ga ho ra gu ru gu ru ma wa tte,wa ta shi ka ra ha na re ru ko ko ro mo,mi e na i wa so u shi ra na i?,ji bun ka ra u go ku ko to mo na ku,to ki no su ki ma ni na ga sa re tsu zu ke te,shi ra na i wa ma wa ri no ko to na do,wa ta shi wa wa ta shi so re da ke,yu me mi te ru? na ni mo mi te na i?,ka ta ru mo mu da na ji bun no ko to ba?,ka na shi mu nan te tsu ka re ru da ke yo,na ni mo kan ji zu su go se ba i i,to ma do u ko to ba a ta e ra re te mo,ji bun no ko ko ro ta da u e no so ra,mo shi wa ta shi ka ra u go ku no na ra ba,su be te ka e ru no na ra ku ro ni su ru,kon na ji bun ni mi ra i wa a ru no?,kon na se ka i ni wa ta shi wa i ru no?,i ma se tsu na i no? i ma ka na shi i no?,ji bun no ko to mo wa ka ra na i ma ma,a yu mu ko to sa e tsu ka re ru da ke yo,hi to no ko to na do shi ri mo shi na i wa,kon na wa ta shi mo ka wa re ru mo na ra,mo shi ka wa re ru no na ra shi ro ni na ru?,na ga re te ku to ki no na ka de de mo,ge da ru sa ga ho ra gu ru gu ru ma wa tte,wa ta shi ka ra ha na re ru ko ko ro mo,mi e na i wa so u shi ra na i?,ji bun ka ra u go ku ko to mo na ku,to ki no su ki ma ni na ga sa re tsu zu ke te,shi ra na i wa ma wa ri no ko to na do,wa ta shi wa wa ta shi so re da ke,yu me mi te ru? na ni mo mi te na i?,ka ta ru mo mu da na ji bun no ko to ba?,ka na shi mu nan te tsu ka re ru da ke yo,na ni mo kan ji zu su go se ba i i,to ma do u ko to ba a ta e ra re te mo,ji bun no ko ko ro ta da u e no so ra,mo shi wa ta shi ka ra u go ku no na ra ba,su be te ka e ru no na ra ku ro ni su ru,u go ku no na ra ba u go ku no na ra ba,su be te ko wa su wa su be te ko wa su wa,ka na shi mu na ra ba ka na shi mu na ra ba,wa ta shi no ko ko ro shi ro ku ka wa re ru?,a na ta no ko to mo wa ta shi no ko to mo,su be te no ko to mo ma da shi ra na i no,o mo i ma bu ta wo a ke ta no na ra ba,su be te ko wa su no na ra ku ro ni na re!!"
times=[768, 768, 768, 768, 768, 768, 768, 768, 672, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 3936, 768, 768, 768, 768, 768, 768, 768, 768, 672, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768, 768]

beats = list(np.array(times)/bpm*15/24)
# math formula for calculating what frame the note should be in.
# (this line code assumes 24 frames per second)

# append 2 because the loop behaves kinda weird if you don't
beats.append(2)

#print(notes_raw) #used for debugging
#print(notes) #used for debugging
#print(beats[1:20]) #used for debugging

screensize = (1280,720)
myclip_arr=[]

dur_arr=beats
print(dur_arr)
l2=lyrics.split(',')
low=0
hi=0
new_arr=dur_arr
lyrics_tight="Ever on and on I continue circling9With nothing but my hate in a carousel of agony9Till slowly I forget and my heart starts vanishing9And suddenly I see that I can't break free- I'm9Slipping through the cracks of a dark eternity9With nothing but my pain and the paralyzing agony9To tell me who I am who I was uncertainty9Enveloping my mind till I can't break free9And maybe it's a dream maybe nothing else is real9But it wouldn't mean a thing if I told you how I feel9So I'm tired of all the pain of the misery inside9And I wish that I could live feeling nothing but the night9You can tell me what to say you can tell me where to go9But I doubt that I would care and my heart would never know9If I make another move there'd be no more turning back9Because everything would change and all will fade to black9Will tomorrow ever come? Will I make it through the night?9Will there ever be a place for the broken in the light?9Am I hurting? Am I sad? Should I stay or should I go?9I've forgotten how to tell did I ever even know?9Can I take another step? I've done everything I can9All the people that I see they will never understand9If I find a way to change if I step into the light9Then I'll never be the same and it all will fade to white9Ever on and on I continue circling9With nothing but my hate in a carousel of agony9Till slowly I forget and my heart starts vanishing9And suddenly I see that I can't break free- I'm9Slipping through the cracks of a dark eternity9With nothing but my pain and the paralyzing agony9To tell me who I am who I was uncertainty9Enveloping my mind till I can't break free9And maybe it's a dream maybe nothing else is real9But it wouldn't mean a thing if I told you how I feel9So I'm tired of all the pain of the misery inside9And I wish that I could live feeling nothing but the night9You can tell me what to say you can tell me where to go9But I doubt that I would care and my heart would never know9If I make another move there'd be no more turning back9Because everything would change and all will fade to black9If I make another move If I take another step9Then it all would fall apart There'd be nothing of me left9If I'm crying in the wind If I'm crying in the night9Will there ever be away? Will my heart return to white?9Can you tell me who you are? Can you tell me where I am?9I've forgotten how to see I've forgotten if I can9If I opened up my eyes there'd be no more going back9'Cause I'd throw it all away and it all will fade to black"

lyrics_tight=lyrics_tight.split('9')

print(len(new_arr))
print(len(lyrics_tight))

for index, ele in enumerate(lyrics_tight):
    txtClip=TextClip(ele,color='white', font="YuGothR", fontsize=40, stroke_width=2, stroke_color='black')
    myclip = CompositeVideoClip([txtClip.set_pos(('center','bottom'))], size=screensize, bg_color=[0x00,0x00,0xFF])
    myclip=myclip.set_duration(new_arr[index])
    myclip_arr.append(myclip)
    if lyrics_tight[index]==lyrics_tight[index-1]:
        print(ele,new_arr[index])


final_clip = concatenate_videoclips(myclip_arr)
final_clip.write_videofile("fullch eng.mp4",fps=24)
myclip.close()
final_clip=[]
prev=VideoFileClip("fullch.mp4")
'''
'''