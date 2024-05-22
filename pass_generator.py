import string
import random
from tkinter import *
from tkinter import messagebox

# ======================= M-1 Using Tkinter ===================================

# Create a Password Generate Function
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def on_gen():
    try:
        length = int(pass_entry.get())
        if length<= 0:
            messagebox.showerror('Error', 'Length of Password should be greater than 0')
            return
        password = gen_pass(length)
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please Enter the Valid Value')

# main window
pass_root = Tk()
pass_root.title('Password Generator')
pass_root.geometry('300x200')
pass_root.config(bg= '#000')

# Create a Label
Label(pass_root,
      text='Enter the Length of Password',
      font=('Times', 14, 'underline', 'bold'),
      fg = '#fff',
      bg= '#000'
    ).pack(pady=10)


# create a Entry Password
pass_entry = Entry(
    pass_root,
    width=15,
    border = 0,
    bg='#fff',
    font=('Arial', 12),
)

pass_entry.pack(pady=10)

gen = PhotoImage(file = 'generate.png')
button = Button(
    pass_root,
    image= gen,
    bg='#000',
    border=0,
    command = on_gen,
)
button.pack(pady=5)


pass_root.mainloop()



# ========================= M-2 Using CMD ====================================
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    while True:
        try:
            length = int(input("Enter the Length of Password : "))
            if length<= 0:
                print('Length of Password should be greater than 0')
                continue
            break

        except ValueError:
            print('Please Enter the Valid Value')

    password = gen_pass(length)
    print(f'Generated Password: {password}')

if __name__ == "__main__":
    main()