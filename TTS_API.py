from gtts import gTTS
import os
import ignitionhack_2020
import 
tts=gTTS(text="awesome",lang="en") #hilights awesome
tts.save("awesome.mp3")
os.system("start awesome.mp3")
