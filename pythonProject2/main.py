from tkinter import *
import file_operations
import text_editor_gui

# главное окно
root = Tk()
root.title('TextPad')
root.geometry("1200x660")

# фрейм для текстового поля
my_frame = Frame(root)
my_frame.pack(pady=5)

# полоса прокрутки для текстового поля
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# текстовое поле
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# связь полосы прокрутки с текстовым полем
text_scroll.config(command=my_text.yview)

# меню
my_menu = Menu(root)
root.config(menu=my_menu)

# Добавьте меню "File" с пунктами "New", "Open", "Save", "Save As" и "Exit"
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_operations.new_file)
file_menu.add_command(label="Open", command=file_operations.open_file)
file_menu.add_command(label="Save", command=file_operations.save_file)
file_menu.add_command(label="Save As", command=file_operations.save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

# меню "Edit" с пунктами "Cut", "Copy", "Paste", "Undo" и "Redo"
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# статусная строка
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Запуск приложения
root.mainloop()
