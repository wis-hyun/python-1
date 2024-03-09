from tkinter import *
from tkinter import messagebox

def myChoice():
    if myVar.get() == 1:
        name='포르쉐'
    elif myVar.get() == 2:
        name='벤츠'
    elif myVar.get() == 3:
        name='BMW'
    elif myVar.get() == 4:
        name='아우디'
    messagebox.showinfo('선택완료', '선택한 차량은 ' + name + '입니다.')

root = Tk()
root.geometry('300x200')

myVar = IntVar()
rb1 = Radiobutton(root, text='포르쉐', variable=myVar, value=1)
rb1.pack()
rb2 = Radiobutton(root, text='벤츠', variable=myVar, value=2)
rb2.pack()
rb3 = Radiobutton(root, text='BMW', variable=myVar, value=3)
rb3.pack()
rb4 = Radiobutton(root, text='아우디', variable=myVar, value=4)
rb4.pack()

button1=Button(root, text='클릭하세요', bg='yellow', command=myChoice)

button1.pack()
root.mainloop()
