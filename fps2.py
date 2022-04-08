# Import

from threading import Thread
import tkinter as tk
from tkinter import * 
from time import sleep, time
import random
from tkinter import scrolledtext
import sys
from tkinter import messagebox


# De window settings

count = 0
window = tk.Tk()
window.geometry("1000x700")
window.title('FPS Trainer')
window.configure(bg='gray')

# De score berekenen

global score
score = 0

# De tijd berekenen

global tijd
tijd = 20



# Functie voor het random laten plaatsen van Labels

def FPStrainer():
    global label_random 
    all_posibilities = ["pressW","pressA","pressS","pressD","pressBalk","oneClick","doubleClick","tripleClick"]
    random_choice_list = random.choice(all_posibilities)
    if random_choice_list == "pressW":
        label_random = Label(window, text = "Press: W", bg = "lightblue", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("w",pressed_label_2)
        label_random.bind("b",reset_label)
    elif random_choice_list == "pressA":
        label_random = Label(window, text = "Press: A", bg = "yellow", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("a",pressed_label_2)
        label_random.bind("b",reset_label)
    elif random_choice_list == "pressS":
        label_random = Label(window, text = "Press: S", bg = "red", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("s",pressed_label_2)
        label_random.bind("b",reset_label)
    elif random_choice_list == "pressD":
        label_random = Label(window, text = "Press: D", bg = "lightgreen", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("d",pressed_label_2)
        label_random.bind("b",reset_label)
    elif random_choice_list == "pressBalk":
        label_random = Label(window, text = "Press: Spacebar", bg = "purple", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,1000), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("<space>",pressed_label_2)
        label_random.bind("b",reset_label)
    elif random_choice_list == "oneClick":
        label_random = Label(window, text = "Single Click", bg = "cyan", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("<Button-1>",pressed_label_1)
        label_random.bind("b",reset_label)
    elif random_choice_list == "doubleClick":
        label_random = Label(window, text = "Double Click", bg = "orange", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("<Double-Button-1>",pressed_label_1)
        label_random.bind("b",reset_label)
    elif random_choice_list == "tripleClick":
        label_random = Label(window, text = "Triple Click", bg = "pink", height = 5, width = 20, relief = "solid", cursor = "cross")
        label_random.place(x=random.randrange(20,900), y = random.randrange(20,600))
        label_random.focus_set()
        label_random.bind("<Triple-Button-1>",pressed_label_1)
        label_random.bind("b",reset_label)

# Functie voor mijzelf om iets te testen

def reset_label(self):
    label_random.destroy()
    FPStrainer()
    
# Functie om een nieuwe random label te plaatsen als de vorige succesvol is uitgevoerd 

def pressed_label_1(self):
    global random_pressed_label, label_random, score
    random_pressed_label = True
    if random_pressed_label == True:
        label_random.destroy()
        score += 1
        scoreLabel.config(text= "Your Score: " + str(score))
        random_pressed_label = False
        FPStrainer()
    else:
        print("wow")

def pressed_label_2(self):
    global random_pressed_label, label_random, score
    random_pressed_label = True
    if random_pressed_label == True:
        label_random.destroy()
        score += 2
        scoreLabel.config(text= "Your Score: " + str(score))
        random_pressed_label = False
        FPStrainer()
    else:
        print("wow")

# Label om de score bij te houden

scoreLabel = Label(window, text="Your Score: " + str(score), bg= "powder blue")
scoreLabel.place(x=50,y=50)

# Functie om de tijd bij te houden

def test():
    global tijd, label_random
    for tijd in range(text_entry,0,-1):
        tijdLabel.config(text= "Your Time : " + str(tijd))
        sleep(1)
    answer_message_box = messagebox.askyesno("Time's over",f"Final score = {score} \nDo you want to play again?")
    label_random.destroy()
    if answer_message_box:
        start_button_begin()
    else:
        window.destroy()


#Label om de tijd bij te houden
tijdLabel = Label(window, text="Your Time : " + str(tijd), bg="powder blue")
tijdLabel.place(x=50,y=100)

# Roept de functie aan & thread      

def start_alles():
    global score
    score = 0
    scoreLabel.config(text= "Your Score: " + str(score))
    button_seconds.destroy()
    button_start_1.destroy()
    entry1.destroy()
    th = Thread(target=FPStrainer)
    th.start()
    th1=Thread(target=test)
    th1.start()

# Button voor het starten als je opnieuw wilt beginnen na het finishen van de vorige game

def start_button_begin():
    global start_button
    start_button= Button(window, text="Click on me to start!",bd=5,command=button_seconds_start)
    start_button.pack(side = 'top')

# Een entry widget

def get_entry_info():
    global text_entry,button_start_1
    text_entry = entry1.get()
    text_entry = int(text_entry)
    button_start_1 = Button(window,text="Click om me to start!",bd=5,command=start_alles)
    button_start_1.pack()

# Button om het aantal seconden te bepalen
def button_seconds_start():
    start_button.destroy()
    global button_seconds, entry1,button_start_1
    button_seconds = Button(window,text="Typ how long you want to last the game! \n If you wrote the seconds in the box please click on me to advance!", bd=5,command=get_entry_info)
    button_seconds.pack()
    entry1 = Entry(window, width=20,bd=5)
    entry1.insert(END, '20')
    entry1.pack()

# Button voor het starten

start_button= Button(window, text="Click on me to edit the seconds!",bd=5,command=button_seconds_start)
start_button.pack(side = 'top')



# Window laten opkomen

window.mainloop()