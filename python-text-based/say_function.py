# --- print text one letter at a time ---


# PYTHON 2 
from sys import stdout
from time import sleep

def say(text):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(0.03)
    print()
    
    
# PYTHON 3
from time import sleep

def say(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.03)
    print()
