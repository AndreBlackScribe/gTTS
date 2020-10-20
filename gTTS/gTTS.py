from gtts import gTTS
import os 


text = "Hello! My name is Boris."
tts = gTTS(text)
tts.save("hi.mp3")

os.system("hi.mp3")
#os.system("hi.mp3")