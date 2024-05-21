from tkinter import *

equation = ""


def show(value):
    global equation
    equation+=value
    result.delete(0, END)
    result.insert(0,equation)

def clear_btn():
    global equation
    equation=""
    result.delete(0, END)

def calculate():
    global equation
    try:
        modified_equation = equation.replace('%', '/100')
        total = str(eval(modified_equation))
        result.delete(0, END) 
        result.insert(0,total)
        equation= total
    except Exception as e:
        result.delete(0, END) 
        result.insert(0,"Error")
        equation =""
        
def backspace():
    global equation
    equation = equation[:-1]
    result.delete(0, END)
    result.insert(0, equation)

    
# Add main window
calc_root = Tk()
calc_root.title('Calculator')
calc_root.geometry('430x500')
calc_root.config(bg= "black")
# calc_root.resizable(0, 0)


result = Entry(
    calc_root,
    font=('Arial', 20, 'bold'),
    width=25,
    fg="#000",
    bg="#fff",
    border= 1,
)
result.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Create all button at one time 
buttons = [
    ('C', 5, 0, clear_btn),
    ('/', 1, 3, lambda: show("/")),
    ('%', 1, 2, lambda: show("%")),
    ('x', 2, 3, lambda: show("*")),
    ('-', 3, 3, lambda: show("-")),
    ('+', 4, 3, lambda: show("+")),
    ('=', 5, 3, calculate),
    ('.', 5, 2, lambda: show(".")),
    ('1', 4, 0, lambda: show("1")),
    ('2', 4, 1, lambda: show("2")),
    ('3', 4, 2, lambda: show("3")),
    ('4', 3, 0, lambda: show("4")),
    ('5', 3, 1, lambda: show("5")),
    ('6', 3, 2, lambda: show("6")),
    ('7', 2, 0, lambda: show("7")),
    ('8', 2, 1, lambda: show("8")),
    ('9', 2, 2, lambda: show("9")),
    ('0', 5, 1, lambda: show("0")),
    ('<', 1, 1, backspace),
]


# Add Properties for buttons
for (text, row, col, cmd) in buttons:
    if text in ['C','/','%','x','-', '+','=','<']:
        fg_clr = "#EE431B"    
    else:
        fg_clr = "#fff"
    Button(
        calc_root,
        text=text,
        command=cmd,
        font=('Arial', 20, 'bold'),
        fg= fg_clr ,
        bg="#000",
        width=3,
        height=1,
        border=0,
    ).grid(row=row, column=col, padx=10, pady=10)


calc_root.mainloop()