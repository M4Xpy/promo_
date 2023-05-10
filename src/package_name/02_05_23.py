import keyboard as keyboard
import pyperclip as pyperclip


def change():
    text = pyperclip.paste()
    diary = {}
    res = ''
    for line in text.splitlines():
        for variable in diary:
            if variable in line:
                line = line.replace(variable, diary[variable])
        if ' = ' in line:
            variable, _, value = line.partition(' = ')
            diary[variable] = value
            line = ''
        if line:
            res += line + '\n'
    pyperclip.copy(str(res))


while True:
    if keyboard.is_pressed('ctrl + c'):
        change()
