#instructions
#import###
from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector

#commands###
def back():
   root.destroy()
   return True

#intializing tk####
root = Tk()
root.title("Instructions")
#frame
frame= Frame(root)
frame.pack()
#canvas
canvas = Canvas(frame, bg="black",width=739,height=415)
canvas.pack()
#images
bg_surface=PhotoImage(file=("mythicon_images/lbinbg.png"))
cloud_surface=PhotoImage(file=("mythicon_images/hitcloud.png"))
go_surface=PhotoImage(file=("mythicon_images/hitgo.png"))
black_surface=PhotoImage(file=("mythicon_images/shadow.png"))
back_surface=PhotoImage(file=("mythicon_images/back.png"))
canvas.create_image(369.5,207.5,image=bg_surface)
canvas.create_image(369.5,80,image=black_surface)
canvas.create_image(30,270,anchor=W,image=cloud_surface)
canvas.create_image(380,270,anchor=W,image=go_surface)
#username file
f=open("mythicon_others/username.txt",'r')
pp=f.read().strip()
f.close()
#text
x=25
y=25
canvas.create_text(x,y,fill="white",font="courier",anchor=W,text="Greetings "+str(pp).title()+'!')
canvas.create_text(x,y+20,fill="white",font="courier",anchor=W,text="The instructions to play the game are simple.DON'T let your dragon hit")
canvas.create_text(x,y+40,fill="white",font="courier",anchor=W,text='the black storm clouds! Press SPACE button to keep your dragon moving.')
canvas.create_text(x,y+60,fill="white",font="courier",anchor=W,text="Your points will be proportional to the duration of your survival.")
canvas.create_text(x,y+80,fill="white",font="courier",anchor=W,text="You are now ready to join the dragon on her mysterious quest.")
canvas.create_text(x,y+100,fill="white",font="courier",anchor=W,text="Happy Flapping!See you around!\(๑╹◡╹๑)ﾉ♬")
#button
Button(root,image=back_surface,command=back,height=40,width=50).place(x=684,y=370)
Button(root,text='SPACE ',font=("courier",8)).place(x=326,y=53)

root.mainloop()#end
