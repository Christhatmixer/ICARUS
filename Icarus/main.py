import pyglet
import sys
import pyaudio
import webbrowser
import serial
import time
import os
import subprocess
import struct
from tkinter import *

# Voice Files optional use
#initialize = pyglet.media.load("Voice-001.wav", streaming=False)
#systemsOnline = pyglet.media.load("systems online.wav", streaming=False)

connected = False
#Find port where arduino is plugged
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




while connected:

    command = arduino.readline()
    lastCommand = b""

    #Initialize
    initialized = 1

    #Main Window
    root = Tk()
    root.title("ICARUS")
    root.geometry("500x500")
    root.resizable(width=False,height=False)

    #Variable
    Entry = StringVar(root)

    #Entry boxes
    siteLabel = Label(root,text="Sites").grid(row=1, column=2)
    enterSite = Label(root,text="Enter Site").grid(row=3,column=1,sticky=W)
    playList = Label(root,text="Enter Playlist").grid(row=5,column=1)
    playListEntry = Entry(root,bd=3).grid(row=5,column=2,sticky=S)
    siteEntry = Entry(root,bd=3).grid(row=3, column=2)
    siteList = Listbox(root).grid(row=2,column=2)


    # GUI commands
    def entry():
        entryVariable = Entry.get()
        siteList.insert(entryVariable)

    #Buttons
    submit = Button(root, text="Submit", command=entry).grid(row=4,column=2)

    root.mainloop()

    while initialized:
        command = arduino.readline()
        if b"Press" in command:
            initialize.play()
            time.sleep(2)
            os.system(r"C:\Users\cfarl_000\Music\Playlists\Love.wpl")
        if b"Light" in command and not (b"Light" in lastCommand):
            webbrowser.open("http://www.worldstarhiphop.com/videos/")
            webbrowser.open("http://lifehacker.com/")
            webbrowser.open("http://espn.go.com/")
            os.startfile(r"C:\Users\cfarl_000\Music\Playlists\Top Rated.wpl")
            lastCommand = b"Light"
            time.sleep(2)
        if b"Dark" in command:
            lastCommand = b""










