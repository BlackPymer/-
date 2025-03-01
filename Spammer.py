import keyboard
import time


def klava_spam():
    a = input("Enter the key to spam (if there are several, separate them with a + sign): ")
    b = int(input("Enter the number of times to spam: "))
    c = float(input("Enter the delay: "))
    d = float(input("Enter the number of seconds before spam: "))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.press_and_release(a)
        keyboard.press_and_release('enter')
        time.sleep(c)

def both_spam():
    a = input("Enter spam text: ")
    e = input("Enter the key to spam (if there are several, separate them with a + sign): ")
    b = int(input("Enter the number of times to spam: "))
    c = float(input("Enter the delay: "))
    d = float(input("Enter the number of seconds before spam: "))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.write(a)
        keyboard.press_and_release(e)
        time.sleep(c)

def spam():
    a = input("Enter spam text: ")
    b = int(input("Enter the number of times to spam: "))
    c = float(input("Enter the delay: "))
    d = float(input("Enter the number of seconds before spam: "))
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
