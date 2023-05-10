from gtts import gTTS
from time import sleep
import os
import pyglet
import keyboard
import time
import pyperclip
import webbrowser
from gtts import gTTS
import re
from googletrans import Translator
import pyglet
from gtts import gTTS
import os
import playsound
import mouse

x = 1
compare = 'eee'


def check_clipboard_data():
    """check clipboards data"""
    global text
    time.sleep(0.01)
    keyboard.send("ctrl + c")
    time.sleep(0.01)
    text = pyperclip.paste()
    time.sleep(0.1)


def saying(text):
    """ audio palying the text"""
    global x, compare
    tts = gTTS(text, lang='ru')
    tts.save(filename := f'C:\\Users\\Я\Desktop\\python_work\\17\\trans\\7-00\\NOW\\downloads\\{x}.mp3')
    x += 1
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)  # prevent from killing
    os.remove(filename)  # remove temperory file


while 1:
    if mouse.is_pressed('left'):
        while mouse.is_pressed('left'):
            pass
        try:
            keyboard.send('ctrl + c')
            check_clipboard_data()
            saying(text)
        except:
            continue








