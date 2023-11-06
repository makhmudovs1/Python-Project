from tkinter import *


def initialize_gui(root, my_text, status_bar):

    my_frame = Frame(root)
    my_frame.pack(pady=5)

    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()

    text_scroll.config(command=my_text.yview)

    status_bar = Label(root, text='Ready         ', anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)
