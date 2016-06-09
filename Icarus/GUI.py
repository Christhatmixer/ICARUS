
import pyglet
import sys
import pyaudio
import webbrowser
import serial
import time
import os
import subprocess
import struct
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

connected = False
arduino = ""
try:
    arduino = serial.Serial("COM5", 9600) #connect to arduino
except:
    #try next port
    try:
        arduino = serial.Serial("COM4", 9600) #connect to arduino
    except:
        #Try next port
        try:
            arduino = serial.Serial("COM3", 9600)
        except:
            #Try next port
            try:
                arduino = serial.Serial("COM3", 9600)
            except:
                try:
                    arduino = serial.Serial("COM2", 9600)
                except:
                    print("No Arduino Found")
                    pass
                else:
                    connected = True

            else:
                connected = True

        else:
            connected = True
    else:
        connected = True
else:
    connected = True

#Main Window
root = Tk()
root.title("ICARUS")
#root.geometry("500x500")
root.resizable(width=False,height=False)

#Variable
EntryR = StringVar(root)
colorValue = StringVar(root)
lastCommand = ""

#Entry boxes
siteLabel = Label(root,text="Sites").grid(row=1, column=2)
enterSite = Label(root,text="Enter Site").grid(row=3,column=1,sticky=W)
playList = Label(root,text="Enter Playlist").grid(row=5,column=1)
playListEntry = Entry(root,bd=3).grid(row=5,column=2,sticky=S)
siteEntry = Entry(root,textvariable=EntryR,bd=3)
siteEntry.grid(row=3, column=2)
siteList = Listbox(root)
siteList.grid(row=2,column=2)

#Connection Status
colorValue.set("red")
connection = Label(root,text = "Connection",bg=colorValue.get())
connection.grid(row=1,column=1)
if connected == True:
    colorValue.set("light green")
else:
    colorValue.set("red")






# GUI commands
def entry():
    entryVariable = EntryR.get()
    siteList.insert(END,entryVariable)

def reconnect():
    try:
        arduino = serial.Serial("COM5", 9600) #connect to arduino
    except:
        #try next port
        try:
            arduino = serial.Serial("COM4", 9600) #connect to arduino
        except:
            #Try next port
            try:
                arduino = serial.Serial("COM3", 9600)
            except:
                #Try next port
                try:
                    arduino = serial.Serial("COM3", 9600)
                except:
                    try:
                        arduino = serial.Serial("COM2", 9600)
                    except:
                        print("No Arduino Found")

                else:
                    connected = True

            else:
                connected = True
        else:
            connected = True
    else:
        connected = True


#Buttons
submit = Button(root, text="Submit", command=entry).grid(row=4,column=2)
reconnectButton = Button(root,text="Reconnnect",command=reconnect)
reconnectButton.grid(column=1,row=2)

try:
    command = arduino.readline()
except:
    pass
try:
    if b"Press" in command:
        #initialize.play()
        time.sleep(2)
        os.system(r"C:\Users\cfarl_000\Music\Playlists\Love.wpl")
except:
    pass
try:
    if b"Light" in command and not (b"Light" in lastCommand):
        for sites in siteList:
            webbrowser.open(sites)
        os.startfile(playListEntry.get)
        lastCommand = b"Light"
        time.sleep(2)
except:
    pass
try:
    if b"Dark" in command:
        lastCommand = b""
except:
    pass


root.mainloop()
