# leaderboard.py 

from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import pygame

# -------------------------------
# Functions
# -------------------------------
def back():
    root.destroy()
    return True


# -------------------------------
# Tkinter setup
# -------------------------------
root = Tk()
root.title("Leader Board")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=739, height=415)
canvas.pack()

# -------------------------------
# Load images safely
# -------------------------------
root.bg_surface = PhotoImage(file=r"mythicon_images/lbinbg.png")
root.lb_surface = PhotoImage(file=r"mythicon_images/board2.png")
root.back_surface = PhotoImage(file=r"mythicon_images/back.png")

canvas.create_image(369.5, 207.5, image=root.bg_surface)
canvas.create_image(450.5, 240, image=root.lb_surface)

# -------------------------------
# Database setup (SQLite)
# -------------------------------
DB_PATH = "mythicon_others/mythiconlogin.db"
if not os.path.exists(DB_PATH):
    messagebox.showerror("Error", "Database not found. Please log in first.")
    root.destroy()
    exit()

mydb = sqlite3.connect(DB_PATH)
cur = mydb.cursor()

# Ensure table exists
cur.execute("""
CREATE TABLE IF NOT EXISTS login (
    username TEXT PRIMARY KEY,
    password TEXT,
    highscore INTEGER DEFAULT 0,
    logindate TEXT
)
""")
mydb.commit()

# -------------------------------
# Fetch top 5 highscores
# -------------------------------
cur.execute("SELECT username, highscore, logindate FROM login ORDER BY highscore DESC LIMIT 5")
top_results = cur.fetchall()

x = 150
y = 210
for user in top_results:
    username_display = user[0].upper()
    highscore_display = user[1]
    date_display = user[2] if user[2] else "N/A"
    canvas.create_text(x, y, fill="black", font=("courier", 20), text=date_display, anchor=W)
    canvas.create_text(x + 130, y, fill="black", font=("courier", 20), text=username_display, anchor=W)
    canvas.create_text(x + 330, y, fill="black", font=("courier", 20), text=str(highscore_display), anchor=W)
    y += 42

# -------------------------------
# Display current user info
# -------------------------------
try:
    with open("mythicon_others/username.txt", "r") as f:
        username = f.read().strip()

    cur.execute("SELECT highscore FROM login WHERE username=?", (username,))
    user_details = cur.fetchone()
    user_highscore = user_details[0] if user_details else 0
    canvas.create_text(140, 40, fill="white", font=("courier", 20),
                       text=f"Username: {username}   Highscore: {user_highscore}", anchor=W)
except FileNotFoundError:
    canvas.create_text(140, 40, fill="white", font=("courier", 20),
                       text="User not logged in", anchor=W)

# -------------------------------
# Back button
# -------------------------------
Button(root, image=root.back_surface, command=back, height=40, width=50).place(x=684, y=370)

root.mainloop()
