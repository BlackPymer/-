from tkinter import *
import time
import keyboard
import strings

spamText = ''
repeat = 0
delay = 0
key = 'Enter'
wait = 0

def spam():
	global spamText, repeat, delay, key, wait
	time.sleep(wait)
	for i in range(repeat):
		keyboard.write(spamText)
		keyboard.press_and_release(key)
		time.sleep(delay)


def Start():
	global spamText, repeat, delay, key, wait
	global spamTextEntry, repeatEntry,delayEntry,keyEntry,waitEntry
	spamText = spamTextEntry.get()
	repeat = int(repeatEntry.get())
	delay = float(delayEntry.get())
	if keyEntry.get() != "":
		key = keyEntry.get()
	wait=int(waitEntry.get())
	spam()

# Interface
root = Tk()
root.title("Spammer")
mainLabel = Label(root,text="Enter settings:",font='Arial 30')

#part 1
spamTextLabel = Label(root,text=strings.spam_text,font='Arial 15')
spamTextEntry = Entry(root,font='Arial 15')
#part 2
repeatLabel = Label(root,text=strings.times_for_spam,font='Arial 15')
repeatEntry = Entry(root,font='Arial 15')
#part 3
delayLabel = Label(root,text=strings.delay,font='Arial 15')
delayEntry = Entry(root,font='Arial 15')
#part 4
keyLabel = Label(root,text=strings.key_for_spam,font='Arial 15')
keyEntry = Entry(root,font='Arial 15')
#part 5
waitLabel = Label(root,text=strings.seconds_before_spam,font='Arial 15')
waitEntry = Entry(root,font='Arial 15')
#button
getInfoButton = Button(root,text = "Начать",command = Start)



mainLabel.pack()
spamTextLabel.pack()
spamTextEntry.pack()
repeatLabel.pack()
repeatEntry.pack()
delayLabel.pack()
delayEntry.pack()
keyLabel.pack()
keyEntry.pack()
waitLabel.pack()
waitEntry.pack()

getInfoButton.pack()
root.mainloop()