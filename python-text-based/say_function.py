# --- print text one letter at a time ---


# Trinket python version
from sys import stdout
from time import sleep

def say(text):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(0.03)
    print()
    
    
# Python 3 version (local dev env)
from time import sleep

def say(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.03)
    print()
