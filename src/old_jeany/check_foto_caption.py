import keyboard
import time
import pyperclip
import webbrowser
from gtts import gTTS
from googletrans import Translator
import pyglet
# import pyautogui


output, in_text = "", ""

def audio():
    try:
        text = in_text
        text = text.replace('_', ' ')
        text = text.split()
        mytext = text
        for t in reversed(mytext):
            if t != "*":
                t = t.lower()
                # Language in which you want to convert
                language = 'en'

                # Passing the text and language to the engine,
                # here we have marked slow=False. Which tells
                # the module that the converted audio should
                # have a high speed
                myobj = gTTS(text=t, lang=language, slow=False)

                # Saving the converted audio in a mp3 file named
                # welcome
                myobj.save(f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media\\{t}.mp3")
    except TypeError:
        pass



def rendering():
    global output, mp3s
    global in_text
    text = in_text
    text += f"  **    {text}  ** "
    text = text.replace('_', ' ')
    letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', ",", ")", "-", ";",
               'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', "'",
               ]
    mp3s = []
    tex = []
    te = []
    ttt = []
    x = 0
    for let in text:
        if let.upper() in letters:
            tex.append(let)
            x += 1
        elif let not in letters and x > 0:
            te.append("".join(tex))
            tex.clear()
            x = 0
    for t in te:
        if t != "sound":
            if t != "rec":
                if t != "mp":
                    if t != "-":
                        if t != "'":
                            if "," not in t:
                                if ")" not in t:
                                    if ";" not in t:
                                        if t.lower() not in ttt:
                                            if t.upper() not in ttt:
                                                ttt.append(t)
                                                t = t.strip()
                                                mp3s.append(f"[sound:{t}.mp3]")

    output = " * " + " * ".join(ttt) + " *"
    in_text = output
    #output += "\n" + "\n".join(mp3s)
    pyperclip.copy(str(output))
    time.sleep(0.2)
    print(output)

def foto():
    text = in_text
    text = text.replace('_', ' ')
    text = text.split()
    tex = text
    for t in reversed(tex):
            if t != "*" :
                t= f'"{t}"'
                tt= f"proverb {t}"
                # time.sleep(random.randint(3, 33) * 0.01)
                #url = f'https://www.google.com/search?q={t}&tbm=isch&ved=2ahUKEwit2J3fyMv7AhUk_CoKHUrnBuEQ2-cCegQIABAA&oq={t}&gs_lcp=CgNpbWcQDDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BAgAEENQlQdYlQdg-w9oAHAAeACAAYABiAHjAZIBAzEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=B-GBY-24CaT4qwHKzpuIDg'
                #url = f'https://www.google.com/search?q={t}&tbm=isch&hl=en&tbs=itp:animated%2Cisz:i&sa=X&ved=0CAQQpwVqFwoTCKi8vsjdzvsCFQAAAAAdAAAAABAE&biw=1349&bih=625'
                url = f'https://www.google.com/search?q={t}&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
                url2 = f'https://www.google.com/search?q={tt}&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
                webbrowser.open(url, new=0, )
                time.sleep(0.1)
                # webbrowser.open(url2, new=0, )
                # time.sleep(0.1)


def translate():
    global in_text
    global wordEN
    translator = Translator()
    in_text = translator.translate(in_text.lower, src='en', dest='ru')
    in_text = in_text.text.upper()
    in_text = in_text + " - "
    pyperclip.copy(str(in_text))

def gooTRA():
    text = in_text
    text = text.replace('_', ' ')
    text = text.split()
    tex = " ".join(text)
    # time.sleep(random.randint(3, 33) * 0.01)
    # url = f'https://www.google.com/search?q={t}&tbm=isch&ved=2ahUKEwit2J3fyMv7AhUk_CoKHUrnBuEQ2-cCegQIABAA&oq={t}&gs_lcp=CgNpbWcQDDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BAgAEENQlQdYlQdg-w9oAHAAeACAAYABiAHjAZIBAzEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=B-GBY-24CaT4qwHKzpuIDg'
    # url = f'https://www.google.com/search?q={t}&tbm=isch&hl=en&tbs=itp:animated%2Cisz:i&sa=X&ved=0CAQQpwVqFwoTCKi8vsjdzvsCFQAAAAAdAAAAABAE&biw=1349&bih=625'
    url = f'https://translate.google.com/?sl=en&tl=ru&text={tex}%0A&op=translate'
    webbrowser.open(url, new=0, )

def online():
    global in_text
    global wordEN
    translator = Translator()
    in_text = translator.translate(in_text, src='en', dest='ru')
    in_text = in_text.text
    if in_text:
        # Language in which you want to convert
        language = 'ru'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=in_text, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        track = f"C:\\Users\\Я\\Desktop\\python_work\\mp3\\{in_text}.mp3"
        myobj.save(track)
        song = pyglet.media.load(track)
        song.play()
        # pyglet.app.run()

        # либо pyglet.media.load(r'D:\Эмиль\Python\timer\zvuki-zvonok_budilnika.mp3')


while True:
    if keyboard.is_pressed('page up'):
        time.sleep(0.01)
        in_text = pyperclip.paste()
        time.sleep(0.1)
        rendering()
        audio()
        time.sleep(0.1)
        keyboard.send("ctrl + v")
        keyboard.send("tab")
        time.sleep(0.1)
        keyboard.send("ctrl + end")
        time.sleep(0.1)
        taba = "\n" + "".join(mp3s) + "\n"
        time.sleep(0.1)
        print(output)
        pyperclip.copy(str(taba))
        time.sleep(0.1)
        keyboard.send("ctrl + v")
        time.sleep(0.3)
        pyperclip.copy(str(output))
        # foto()###########
        time.sleep(0.1)
        time.sleep(1)
    # if keyboard.is_pressed('w'):
    #     pyautogui.rightClick()
    #     time.sleep(0.01)
    #     for x in range(4):
    #         keyboard.press("up")
    #         time.sleep(0.01)
    #     keyboard.press("enter")
    if keyboard.is_pressed('alt'):
        in_text = pyperclip.paste()
        foto()
        time.sleep(2)

    if keyboard.is_pressed('end'):
        in_text = pyperclip.paste()
        gooTRA()
        time.sleep(2)
    if keyboard.is_pressed('home'):
        keyboard.send("ctrl + c")
        in_text = pyperclip.paste()
        online()
        #time.sleep(0.1)
        print(in_text)
        #time.sleep(1)
    if keyboard.is_pressed('page down'):
        time.sleep(0.01)
        keyboard.send("tab")
        time.sleep(0.01)
        keyboard.send("tab")
        time.sleep(0.01)
        keyboard.send("enter")
        time.sleep(0.01)
        # keyboard.send("ctrl + v")
        # time.sleep(0.1)
        # keyboard.send("ctrl + home")
        # keyboard.send("ctrl + a")
        # time.sleep(0.1)
        # keyboard.send("ctrl + c")
        # time.sleep(0.1)
        in_text = pyperclip.paste()
        time.sleep(0.1)
        split_text = in_text.split()
        time.sleep(0.01)
        title = ""
        for letter in split_text[0]:
            if letter != "_":
                title += f"{letter}"
            elif letter == "_":
                break
        time.sleep(0.01)
        keyboard.write(" * " + split_text[0] + " * " + f"[sound:{title}.mp3]")
        time.sleep(0.01)
        keyboard.send("tab")
        time.sleep(0.01)
        translator = Translator()
        total = []

        trans = f"{title.lower()}"
        translated = translator.translate(trans, src='en', dest='ru')
        total.append(translated.text.upper())
        print(translated.text.upper())

        trans = f"the {title.lower()} "
        translated = translator.translate(trans, src='en', dest='ru')
        if translated.text.upper() not in total:
            total.append(translated.text.upper())
        print(translated.text.upper())

        trans = f"to {title.lower()} "
        translated = translator.translate(trans, src='en', dest='ru')
        adj = translated.text.upper()
        too = adj
        if too not in total:
            total.append(too)
        print(adj)

        trans = f"too {title.lower()} "
        translated = translator.translate(trans, src='en', dest='ru')
        adj = translated.text.upper()
        adjective = adj.split()
        too = adjective[1:]
        too = " ".join([str(a) for a in too])
        if too not in total:
            total.append(too)
        print(adj, too)
        keyboard.write("\n_" + "____".join([str(s) for s in total]) + "_\n\n")
        time.sleep(0.01)
        keyboard.send("ctrl + v")
        # time.sleep(0.1)
        # keyboard.write(f"[sound:{title}.mp3]")
        # time.sleep(0.1)
        # for x in range(10):
        #     keyboard.send("tab")
        #     time.sleep(0.2)









