import keyboard
import time
import strings 

def klava_spam():
    a = input(strings.key_for_spam)
    b = int(input(strings.times_for_spam))
    c = float(input(strings.delay))
    d = float(input(strings.seconds_before_spam))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.press_and_release(a)
        keyboard.press_and_release('enter')
        time.sleep(c)

def both_spam():
    a = input(strings.spam_text)
    e = input(strings.key_for_spam)
    b = int(input(strings.times_for_spam))
    c = float(input(strings.delay))
    d = float(input(strings.seconds_before_spam))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.write(a)
        keyboard.press_and_release(e)
        time.sleep(c)

def spam():
    a = input(strings.spam_text)
    b = int(input(strings.times_for_spam))
    c = float(input(strings.delay))
    d = float(input(strings.seconds_before_spam))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.write(a)
        keyboard.press_and_release('enter')
        time.sleep(c)

while True:
    print("")
    tip = int(input("Do you want to spam with text(1), keys(2) or mixed(3)? "))
    if tip == 1:
        spam()
    elif tip == 3:
        both_spam()
    else:
        klava_spam()
