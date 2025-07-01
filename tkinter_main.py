# tkinter 임포트
import tkinter

# tkinter 초기 설정
root = tkinter.Tk()
root.title('Dol Lim Pan')
root.geometry('800x600')
root.resizable(False, False)

input_list = []

# 객체 클래스 정의
class Item:
    def __init__(self, master, value, index):
        self.value = value
        self.label = tkinter.Label(master, text=f'{index} : {value}')
        self.label.pack()

def add_input():
    value = entry.get()
    input_list.append(value)
    entry.delete(0, tkinter.END)
    render_objects()

def render_objects():
    for widget in frame.winfo_children():
        widget.destroy()
    for i, val in enumerate(input_list):
        Item(frame, val, i)

entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text='추가', command=add_input)
button.pack()

frame = tkinter.Frame(root)
frame.pack(fill='both', expand=True)

# 종료할 때까지 계속 실행
root.mainloop()