import sqlite3
from tkinter import *
from PIL import Image
from tkinter import messagebox
from subprocess import call
import pygame
import os

# --- Create / connect to SQLite database ---
os.makedirs("mythicon_others", exist_ok=True)
conn = sqlite3.connect("mythicon_others/mythiconlogin.db")
cur = conn.cursor()

# --- Create table if it doesn't exist ---
cur.execute("""
CREATE TABLE IF NOT EXISTS Login (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE,
    Password TEXT,
    logindate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()



# --- Commands ---
def loginbutton():
    username = e1.get().strip()
    password = e2.get().strip()

    if username == "" or password == "":
        messagebox.showinfo('', "All fields are required")
        return False

    cur.execute("SELECT * FROM Login WHERE Username=? AND Password=?", (username, password))
    results = cur.fetchall()

    if results:
        messagebox.showinfo('', "Login Successful!")
        uname = username
        with open("mythicon_others/username.txt", 'w') as f:
            f.write(uname)

        root.destroy()

        

        # Launch main game
        call(['python', 'startpage.py'])
        return True
    else:
        messagebox.showinfo('', "Invalid Username and Password")
        return False


def registerbutton():
    username = e1.get().strip()
    password = e2.get().strip()

    if username == "" or password == "":
        messagebox.showinfo('', "All fields are required")
        return False

    cur.execute("SELECT * FROM Login WHERE Username=?", (username,))
    results = cur.fetchall()

    if results:
        messagebox.showinfo('', 'Username taken')
        return False
    else:
        cur.execute("INSERT INTO Login (Username, Password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo('', 'Registration Successful!')
        return True


# --- Main segment ---
root = Tk()
root.title("Login")

# Frame
frame = Frame(root)
frame.pack()

# Canvas
canvas = Canvas(frame, bg="black", width=739, height=415)
canvas.pack()

# --- Images ---
bg_image = PhotoImage(file="mythicon_images/peakpx.png")
username_image = PhotoImage(file="mythicon_images/uname.png")
password_image = PhotoImage(file="mythicon_images/pasword.png")
login_image = PhotoImage(file="mythicon_images/login.png")
register_image = PhotoImage(file="mythicon_images/register.png")
loginpg_image = PhotoImage(file="mythicon_images/loginpage.png")

# --- Canvas Elements ---
canvas.create_image(369.5, 207.5, image=bg_image)
canvas.create_image(380, 70, image=loginpg_image)
canvas.create_image(250, 150, image=username_image)
canvas.create_image(250, 200, image=password_image)
canvas.create_text(
    380, 250,
    fill="white",
    font="courier",
    text="Please enter your details before logging in or registering."
)

# --- Entry fields ---
global e1, e2, uname
e1 = Entry(root, font=("courier", 15))
e1.place(x=400, y=135, width=200, height=28)

e2 = Entry(root, font=("courier", 15), show="*")
e2.place(x=400, y=185, width=200, height=28)

# --- Buttons ---
Button(root, image=login_image, command=loginbutton, height=40, width=150).place(x=140, y=300)
Button(root, image=register_image, command=registerbutton, height=40, width=220).place(x=375, y=300)

root.mainloop()

