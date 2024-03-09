from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo('처음', '환영합니다. 홈페이지입니당!')

root = Tk()
root.geometry('300x100')

button1 = Button(root, text='클릭하세요', fg='red', command=myFunc)
button1.pack()

root.mainloop()
 
