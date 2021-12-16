# import modules needed for this script
from tkinter import *
import os


# Shutdown function
def shutdown():
    return os.system('shutdown /s /t 1')


# Restart function
def restart():
    return os.system('shutdown /r /t 1')


# Logout function
def logout():
    return os.system('shutdown -l')


# TK object
master = Tk()
master.geometry('350x350')
master.title(string='Power Control Unit')

# Background color
master.configure(bg='#FFFFFF')

# Create buttons
# Shutdown button
Button(master,
       text='Shutdown',
       command=shutdown,
       height=2, width=8,
       bg='#FFFFFF',
       fg='#111111',
       font=('arial bold', 14),
       borderwidth=3,
       relief='raised',
       padx=5,
       pady=10).pack(padx=5, pady=10)

# Restart button
Button(master,
       text='Restart',
       command=restart,
       height=2,
       width=8,
       bg='#FFFFFF',
       fg='#111111',
       font=('arial bold', 14),
       borderwidth=3,
       relief='raised',
       padx=5,
       pady=10).pack(padx=5, pady=10)

# Logout button
Button(master,
       text='Log Out',
       command=logout,
       height=2,
       width=8,
       bg='#FFFFFF',
       fg='#111111',
       font=('arial bold', 14),
       borderwidth=3,
       relief='raised',
       padx=5,
       pady=10).pack(padx=5, pady=10)

# Main Application Function
mainloop()
