import os
from tkinter import *
from tkinter import messagebox

# Add main window
todo_root = Tk()
todo_root.title('To-Do List')
todo_root.geometry('550x400')
todo_root.resizable(0, 0)

# Create a frame
lframe = Frame(todo_root)
lframe.pack(pady=10, padx=10, fill=X)

# Create a Label
Label(lframe, text='Task-1 To-Do List', font=('arial', 20, 'bold'),underline=0).pack(pady=10)

frame = Frame(todo_root)
frame.pack(pady=10, padx=10)

# Create a list
lb = Listbox(
    frame,
    width= 20,
    height= 8,
    font= ('serif', 12, 'bold'),
    bd = 0,
    fg = "#000",
    selectbackground= "grey",
    activestyle= "underline",
)
lb.pack(side=LEFT, fill=BOTH, pady=5)

# Create a scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Create to load function
def loadTask():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            for i in tasks:
                lb.insert(END, i.strip())

# Create Save function for Saving the tasks in file
def saveTask():
    with open('tasks.txt', 'w') as file:
         tasks = lb.get(0, END)
         for task in tasks:
             file.write(task + "\n")

# Call Load task
loadTask()

# Create to enter user task
new = Entry(
    todo_root,
    font=('serif', 12, 'bold'),
    borderwidth=3, 
    relief="groove",

)

new.pack(pady=8)

# Create function
def addTask():
    task = new.get()
    if task != "":
        lb.insert(END, task)
        new.delete(0,"end")
    else:
        messagebox.showwarning("warning", "Please Enter Task..")

def dltTask():
    lb.delete(ANCHOR)


# Add one more frame
button = Frame(todo_root)
button.pack(pady=4)

add = PhotoImage(file = 'add.png')
add_btn = Button(
    button,
    image= add,
    padx= 5,
    border= 0,
    command= addTask,
)
add_btn.pack(fill=BOTH, expand=True,side=LEFT)

dlt = PhotoImage(file = 'dlt.png')
dlt_btn = Button(
    button,
    image= dlt,
    padx=5,
    border= 0,
    command=dltTask,
)
dlt_btn.pack(fill=BOTH, expand=True,side=LEFT)

# Call the function to destroy the application
todo_root.protocol('WM_DELETE_WINDOW', lambda: [saveTask(), todo_root.destroy()])

todo_root.mainloop()