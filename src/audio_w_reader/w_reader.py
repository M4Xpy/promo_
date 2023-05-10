import re
from datetime import time
from time import sleep

import mouse as mouse
from gtts import gTTS
import keyboard as keyboard
import pyglet as pyglet
import pyperclip as pyperclip




counter = 0
def saying(counter, text):
    """ audio palying the text"""

    tts = gTTS(text, lang='en')
    filename = f'C:\\Users\\Я\Desktop\\python_work\\17\\trans\\7-00\\NOW\\downloads\\{counter}.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()



    # sleep(music.duration)  # prevent from killing
    # os.remove(filename)  # remove temperory file

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('ctrl + c'):
            text = pyperclip.paste()
            counter += 1
            saying(counter, text)


