from gtts import gTTS
from playsound import playsound
import time
import os
from interface import CountDownInterface
countdowninterface = CountDownInterface.CountDownInterface()
def speak(text):
    tts = gTTS(text=text, lang='en')

    filename = './mp3_file/'+text+'.mp3'
    if not (os.path.exists(filename)):
        tts.save(filename)
    playsound(filename)

    return True


def time_count(second):
    countdowninterface.countdown(second)