import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string

global root, result_label, copy_button
entry=None
com = None

def Rock():
    entry='ROCK'
    game(entry)

def paper():
    entry='PAPER'
    game(entry)
def scissor():
    entry='SCISSOR'
    game(entry)


def game(input):
    global result_label,result_label1,com,result_label2
    result_label.config(text=f"Player: {input}")
    com=random.choice(['ROCK','PAPER','SCISSOR'])
    result_label1.config(text=f"COMPUTER: {com}")
    if input==com:
        result= 'TIE'
        result_label2.config(text=f" {result}")
    else:
        if input=='PAPER' and com =='ROCK':
            result='YOU WON'
        elif input=='ROCK' and com =='SCISSOR':
            result='YOU WON'
        elif input=='SCISSOR' and com=='PAPER':
            result='YOU WON'
        else:
            result='COMPUTER WON'
        result_label2.config(text=f" {result}")




if __name__=='__main__':

    # Create the main application window
    root = tk.Tk()
    root.title("Rock Paper scissor")

    # Create and place the widgets


    generate_button = tk.Button(root, text="Rock",command=Rock)
    generate_button.pack(side=tk.LEFT,padx=10,pady=20)
    generate_button = tk.Button(root, text="paper",command=paper)
    generate_button.pack(side=tk.LEFT,padx=10,pady=20)
    generate_button = tk.Button(root, text="Scissor",command=scissor)
    generate_button.pack(side=tk.LEFT,padx=10,pady=20)

    result_label2 = tk.Label(root, text="", font=("Helvetica", 20), wraplength=400,fg='red')
    result_label2.pack(padx=10, pady=20, side=tk.BOTTOM)

    result_label1 = tk.Label(root, text="", font=("Helvetica", 12,), wraplength=400)
    result_label1.pack(padx=10,pady=20,side=tk.BOTTOM)


    result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
    result_label.pack(padx=10,pady=20,side=tk.BOTTOM)


    root.mainloop()