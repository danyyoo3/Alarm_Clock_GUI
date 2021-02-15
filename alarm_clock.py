from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime
from pygame import mixer


current = datetime.datetime.now()
hour = int(input("What hour?"))
minute = int(input("What minutes?"))
dn = input("AM/PM?")

if dn == "AM":
    if hour >= 12:
        invalid_command(str(hour))
    else:
        alarm_time = datetime.datetime(current.year, current.month, current.day, hour, minute)

elif dn == "PM":
    if hour >= 12:
        alarm_time = datetime.datetime(current.year, current.month, current.day, hour, minute)
    elif hour < 12:
        alarm_time = datetime.datetime(current.year, current.month, current.day, hour + 12, minute)
    
while True:
    temp = datetime.datetime.now()
    if temp == alarm_time:
        mixer.init()
        mixer.music.load(r'C:\Users\HJ Dany Yoo\Documents\Projects\(BTS) - Not Today.mp3')
        mixer.music.play()


master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()


##To select music file to play
#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
