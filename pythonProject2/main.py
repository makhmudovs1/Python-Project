from tkinter import *
from tkinter import filedialog
from tkinter import font
import os

root = Tk()
root.title('TextPad')
root.geometry("1200x660")

# Set variable for open file name
global open_status_name
open_status_name = False


# Create New File Function
def new_file():
    # Delete previous text
    my_text.delete("1.0", END)
    # Update status bars
    root.title('New File - TextPad')
    status_bar.config(text="New File         ")

    global open_status_name
    open_status_name = False


# Open Files
def open_file():
    # Delete previous text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*html"), ("Python Files", "*,py"), ("All Files", "*.*")))

    # Check to see if there is a file
    if text_file:
        # Make filename global so we can
        global open_status_name
        open_status_name = text_file

    # Update Status bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("", "")
    root.title(f'{name} - TextPad!')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()


# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Save File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if text_file:
        # Update Status Bar
        name = text_file
        status_bar.config(text=f'Saved:{name}        ')
        name = name.replace("", "")
        root.title(f'{name} - TextPad!')
        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close The File
        text_file.close()


# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close The File
        text_file.close()
        # Update Status Bar
        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        # Prompt user to save the file with a new name
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_name:
            open_status_name = file_name
            # Save the file with the new name
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))
            # Close The File
            text_file.close()
            # Update Status Bar
            status_bar.config(text=f'Saved: {open_status_name}        ')


# Exit
def exit_app():
    root.quit()


# Create main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box

my_text = Text(my_frame, width=97, height=25, font=("Helvetica",16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: my_text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: my_text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: my_text.event_generate("<<Paste>>"))
edit_menu.add_command(label="Undo", command=lambda: my_text.event_generate("<<Undo>>"))
edit_menu.add_command(label="Redo", command=lambda: my_text.event_generate("<<Redo>>"))

# Add Status Bar To Bottom Of App
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()