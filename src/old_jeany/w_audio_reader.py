import keyboard
import time
import pyperclip
import webbrowser
from gtts import gTTS
import re
from googletrans import Translator
import pyglet


# import pyautogui

def check_clipboard_data():
    """check clipboards data"""
    global input
    time.sleep(0.01)
    keyboard.send("ctrl + c")
    time.sleep(0.01)
    input = pyperclip.paste()
    time.sleep(0.1)


l = 0


def check_sentence():
    """ get short sentence"""
    global output, l, sl
    sl = ""
    split_regex = re.compile(r'[.|!|?|…|,|:|;|(|)|`|\n]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(input)])
    for s in sentences:
        if len(s) > 3:
            # if len(s) < 15:
            #     sl += s
            # elif len(s) > 14:
            sl += s
            translator = Translator()
            translated = translator.translate(sl, src='en', dest='ru')
            output = translated.text  + "\n" + sl.upper()
            print(output)
            try:
                t = translated.text
                language = 'ru'
                myobj = gTTS(text=t, lang=language, slow=False)
                myobj.save(f"C:\\Users\\Я\\Desktop\\python_work\\17\\trans\\7-00\\NOW\\downloads\\{l}.mp3")
                l += 1
                t = sl
                language = 'en'
                myobj = gTTS(text=t, lang=language, slow=True)
                myobj.save(f"C:\\Users\\Я\\Desktop\\python_work\\17\\trans\\7-00\\NOW\\downloads\\{l}.mp3")
                l += 1
                sl = ""
            except TypeError:
                pass


while True:
    if keyboard.is_pressed('page up'):
        check_clipboard_data()
        check_sentence()
