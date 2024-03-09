from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

root = Tk()
root.geometry('200x200')
label1=Label(root,text='선택된 파일 이름')
label1.pack()

extName = askstring('확장명', '확장명을 입력(ex : hwp, png, zip등)')
filename = askopenfilename(parent=root, filetypes=(('입력파일','*.'+extName),('모든파일','*.*')))
label1.configure(text=str(filename))

root.mainloop()