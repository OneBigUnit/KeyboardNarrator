from sound import Sound
import keyboard
import string
import time
import os


EXIT_KEY = "<NOT A KEY>"


def get_paths():
    sound_paths = []
    for data in os.walk('KeyboardSounds'):
        dir_path, folders, files = data

        for f in files:
            if f.lower().endswith('.mp3'):
                sound_paths.append(os.path.join(dir_path, f))
    return sound_paths


def generate_structures(sound_paths):
    symbols = list(string.printable[:-2].rstrip().replace("\"", "").replace("*", "").replace(":", "").replace("\\", "")
                   .replace(".", "").replace("/", "").replace("<", "").replace(">", "").replace("|", "")
                   .replace(">", "").replace("¬", "").replace("?", "")) + [
        "*", "\\", ":", ".", ">", "<", "¬", "|", "?", "/", "\"", "alt gr", "alt", "backspace", "caps lock",
        "ctrl", "delete", "end", "enter", "esc", "home", "insert", "menu", "num lock", "page up", "page down",
        "pause", "print screen", "right control", "right shift", "scroll lock", "shift", "tab", "left", "right", "up",
        "down", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"
    ]
    names = list(string.printable[:-2].rstrip().replace("\"", "").replace("*", "").replace(":", "").replace("\\", "")
                 .replace(".", "").replace("/", "").replace("<", "").replace(">", "").replace("|", "")
                 .replace(">", "").replace("¬", "").replace("?", "")) + [
        "asterisk", "backslash", "colon", "full stop", "greater", "less", "not sign", "pipe", "question",
        "slash", "speech", "alt gr", "alt", "backspace", "caps lock", "ctrl", "delete", "end", "enter", "esc",
        "home", "insert", "menu", "num lock", "page up", "page down", "pause", "print screen", "ctrl", "shift",
        "scroll lock", "shift", "tab", "left", "right", "up", "down", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
        "f9", "f10", "f11", "f12"
    ]
    keys = {symbol: name for symbol, name in zip(symbols, names)}
    keyboard_sounds = {}
    for key in keys.values():
        for path in sound_paths:
            if f"{key}.mp3" == path.split("\\")[-1]:
                keyboard_sounds[key] = Sound(path)
    return keys, keyboard_sounds


def narrate(keys, keyboard_sounds):
    while (key := keyboard.read_key()) != EXIT_KEY:
        if keys.get(key) in keyboard_sounds:
            try:
                keyboard_sounds.get(keys.get(key)).play(from_path="KeyboardSounds")
            except ValueError:
                pass
        time.sleep(0.08)


def main(sound_paths):
    keys, keyboard_sounds = generate_structures(sound_paths)
    while True:
        narrate(keys, keyboard_sounds)


if __name__ == "__main__":
    main(get_paths())
