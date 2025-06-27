from tkinter import *

count = 0

root = Tk()
root.title('Dol Lim Pan')
root.geometry('800x600')
root.resizable(False, False)

def countplus():
    global count
    count += 1
    label.config(text=str(count))

def countminus():
    global count
    count -= 1
    label.config(text=str(count))

label = Label(root, text='0')
label.pack()

button_plus = Button(root, width=10, text='Plus', overrelief='solid', command=countplus)
button_plus.pack()

button_minus = Button(root, width=10, text='Minus', overrelief='solid', command=countminus)
button_minus.pack()

root.mainloop()