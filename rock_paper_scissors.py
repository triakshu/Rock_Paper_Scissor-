import random
from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk


def orange_theme():
    yo.configure(background='orange')


yo = tk.ThemedTk()  # setting theme
yo.get_themes()
yo.set_theme('plastik')
orange_theme()


def red_theme():
    yo.configure(background='red')


def yellow_theme():
    yo.configure(background='yellow')


def blue_theme():
    yo.configure(background='blue')


def green_theme():
    yo.configure(background='green')


menu_bar = Menu(yo)  # adding Menu Bar
yo.config(menu=menu_bar)

submenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Themes', menu=submenu)
submenu.add_command(label='Red', command=red_theme)
submenu.add_command(label='Yellow', command=yellow_theme)
submenu.add_command(label='Blue', command=blue_theme)
submenu.add_command(label='Green', command=green_theme)
submenu.add_command(label='Default', command=orange_theme)

root = Frame(yo)
root.pack(fill=BOTH, expand=True)
choose = ttk.Label(root, text='CHOOSE ONE', font='Arial 25')
choose.pack(pady=30)

yo.title('Rock Paper Scissor')  # adding title of GUI
user = None


def decide():
    global computer
    computer = random.choice(['Rock', 'Paper', 'Scissor'])  # CPU decision
    go()


permanent = ttk.Label(root, text='', font='Arial 15 bold')
permanent.pack(pady=20)

yipe = ttk.Label(root, text='')
yipe.pack()
yey = ttk.Label(root, text='')
yey.pack()


def again():
    permanent['text'] = ''
    yipe['text'] = ''
    yey['text'] = ''
    rockbutton.config(state=NORMAL)
    paperbutton.config(state=NORMAL)
    scissorbutton.config(state=NORMAL)


restart = ttk.Button(root, text='RESTART ?', command=again)
restart.pack(pady=40, padx=80)
restart.config(state=DISABLED)


def blank():
    rockbutton.config(state=DISABLED)
    paperbutton.config(state=DISABLED)
    scissorbutton.config(state=DISABLED)
    restart.config(state=NORMAL)


def computers():
    permanent['text'] = '"COMPUTER WON"'
    blank()


def users():
    permanent['text'] = '"YOU WON"'
    blank()


def compulsory():
    yipe['text'] = 'User is {}'.format(user)
    yey['text'] = 'Computer is {}'.format(computer)


def draw():
    permanent['text'] = '"DRAW"'
    blank()


# GAME CODE

def go():
    if user == computer:
        compulsory()
        draw()
    if user == 'Rock':
        if computer == 'Paper':
            compulsory()
            computers()
        elif computer == 'Scissor':
            compulsory()
            users()
    if user == 'Paper':
        if computer == 'Scissor':
            compulsory()
            computers()
        elif computer == 'Rock':
            compulsory()
            users()
    if user == 'Scissor':
        if computer == 'Rock':
            compulsory()
            computers()
        elif computer == 'Paper':
            compulsory()
            users()


def rock():
    global user
    user = 'Rock'
    decide()


def paper():
    global user
    user = 'Paper'
    decide()


def scissor():
    global user
    user = 'Scissor'
    decide()


# Buttons dclaration

rockphoto = PhotoImage(file='images/rock.png')
rockbutton = ttk.Button(image=rockphoto, command=rock)
rockbutton.pack(padx=200)

paperphoto = PhotoImage(file='images/paper.png')
paperbutton = ttk.Button(image=paperphoto, command=paper)
paperbutton.pack(pady=20)

scissorphoto = PhotoImage(file='images/scissor.png')
scissorbutton = ttk.Button(image=scissorphoto, command=scissor)
scissorbutton.pack(pady=10)

root.mainloop()
