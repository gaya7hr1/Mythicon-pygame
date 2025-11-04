#start page
#import####
from tkinter import *
from tkinter import messagebox
from subprocess import call
import pygame

#commands####
def start():
    root.destroy()
    pygame.mixer.music.stop()
    call(['python','gamecode.py'])
    return True
def leaderboard():
    call(['python','leaderboard.py'])
    return True
def instructions():
    call(['python','instructions.py'])
    return True

#intializing tk####
root = Tk()
root.title("MYTHICON")
#pygame####
pygame.mixer.init()# initialise the pygame
pygame.mixer.music.load("mythicon_sounds/skycol.wav")
pygame.mixer.music.play(-1)
#frame
frame= Frame(root)
frame.pack()
#canvas
canvas = Canvas(frame, bg="black",width=739,height=415)
canvas.pack()
#images
bg_surface= PhotoImage(file =("mythicon_images/pink.png"))
title_image=PhotoImage(file = ("mythicon_images/title.png"))

#open file username
f=open("mythicon_others/username.txt",'r')
pp=f.read().strip()
f.close()
canvas.create_image(369.5,207.5,image=bg_surface)
canvas.create_image(369.5,150,image=title_image)

#text
txt='WELCOME BACK ' + str(pp).upper() +'! we await your grand entrance into the magical realm of dragons '.upper()
canvas.create_text(655,370,fill="white",font=("courier",13),text=('CREDITS :\nJ.GAYATHRI\nA.R KEERTHANA\nP.YESHASWI'))
canvas.create_text(30,40,fill="white",font=("courier",11),anchor=W,text=(txt))
#buttons
Button(root,text='START',font=('courier',15),width=15,command=start).place(x=300,y=300)
Button(root,text='LEADERBOARD',font=('courier',15),width=15,command=leaderboard).place(x=300,y=350)
Button(root,text='INSTRUCTIONS',font=('courier',15),width=15,command=instructions).place(x=300,y=250)

root.mainloop()#end
