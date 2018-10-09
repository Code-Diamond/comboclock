#!/usr/bin/python3
from tkinter import *
import tkinter as tk
import datetime
import math
# create a Tk window
root = tk.Tk() 
#put title in center
def center(e):
    w = int(root.winfo_width() / 3.5) # get root width and scale it ( in pixels )
    s = 'Clock'.rjust(w//2)
    root.title(s)
root.bind("<Configure>", center) 
root.resizable(False, False)

canvas = Canvas(root, width = 400, height = 400, bg='#332f28')
currentDT = datetime.datetime.now()
time = currentDT.strftime("%I:%M:%S %p")
hour = datetime.datetime.now().hour;
minute = datetime.datetime.now().minute;
second = datetime.datetime.now().second;
canvas.create_text(197,50, tag="timestamp",fill="#65FF00",font='Verdana 41 bold', text=time)

canvas.pack()
radius = 125
xBeg=68
xEnd=318
yBeg=105
yEnd=355
centerX=((xBeg+xEnd)/2)
centerY=((yBeg+yEnd)/2)
#clock backboard
canvas.create_oval(xBeg, yBeg, xEnd, yEnd,tag="clock", width=10, fill="#1d1e1d")#65FF00
#clock hour hand
canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(hour * 30))),  centerY - (radius*math.cos(math.radians(hour*30))), width=10, fill="#0d5b06", tag="hourHand")
#clock minute hand
canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(minute * 6))),  centerY - (radius*math.cos(math.radians(minute*6))), width=5, fill="yellow", tag="minuteHand")
#clock second hand
canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(second * 6))),  centerY - (radius*math.cos(math.radians(second*6))), width=2, fill="red", tag="secondHand")
#clock middle circle
canvas.create_oval(centerX-7, centerY-7, centerX+7, centerY+7,tag="clockInnerCircle", width=7, fill="black")#65FF00
# update function for clock
def update_label():
	#update digital clock
	currentDT = datetime.datetime.now()
	time = currentDT.strftime("%I:%M:%S %p")
	hour = datetime.datetime.now().hour;
	minute = datetime.datetime.now().minute;
	second = datetime.datetime.now().second;
	canvas.itemconfig("timestamp", text=time)

	#add time markings
	canvas.create_text(194,115, fill="#65FF00",font='Verdana 12', text="12")
	canvas.create_text(308,230, fill="#65FF00",font='Verdana 12', text="3")
	canvas.create_text(193,342, fill="#65FF00",font='Verdana 12', text="6")
	canvas.create_text(78,230, fill="#65FF00",font='Verdana 12', text="9")
	#update analog
	canvas.delete(canvas.gettags("hourHand"))
	canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(hour * 30))),  centerY - (radius*math.cos(math.radians(hour*30))), width=10, fill="#0d5b06", tag="hourHand")
	canvas.delete(canvas.gettags("minuteHand"))
	canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(minute * 6))),  centerY - (radius*math.cos(math.radians(minute*6))), width=5, fill="yellow", tag="minuteHand")
	canvas.delete(canvas.gettags("secondHand"))
	canvas.create_line(centerX, centerY, centerX + (radius*math.sin(math.radians(second * 6))),  centerY - (radius*math.cos(math.radians(second*6))), width=2, fill="red", tag="secondHand")
	canvas.delete(canvas.gettags("clockInnerCircle"))
	canvas.create_oval(centerX-7, centerY-7, centerX+7, centerY+7,tag="clockInnerCircle", width=7, fill="black")#65FF00
	root.after(1000, update_label)

#Place window in middle
w = 395 # width for the Tk root
h = 380 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# run recursive update function
update_label()


root.mainloop() # starts the mainloop
