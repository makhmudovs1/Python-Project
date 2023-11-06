from tkinter import filedialog, END

open_status_name = False


def open_file(my_text, status_bar, root):
    my_text.delete("1.0", END)

    text_file = filedialog.askopenfilename(initialdir="", title="Open File",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    if text_file:
        global open_status_name
        open_status_name = text_file

    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("", "")
    root.title(f'{name} - TextPad!')

    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def save_as_file(my_text, status_bar, root):
    text_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="", title="Save File",
                                             filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved:{name}        ')
        name = name.replace("", "")
        root.title(f'{name} - TextPad!')
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


def save_file(my_text):
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    else:
        save_as_file(my_text)


def new_file(my_text, root, status_bar):
    my_text.delete("1.0", END)
    root.title('New File - TextPad')
    status_bar.config(text="New File         ")
    global open_status_name
    open_status_name = False
