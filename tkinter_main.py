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
        self.button = tkinter.Button(master, text=value, command=lambda: self.delete(index))
        self.button.pack()


    def delete(self, index):
        del input_list[index]
        render_objects()

# 리스트에 입력값 추가
def add_input():
    value = entry.get()
    if value != '여기에 입력하세요' and value != '':
        input_list.append(value)
        entry.delete(0, tkinter.END) # 입력창 비우기
        render_objects()

# 리스트 객체 렌더링
def render_objects():
    for widget in frame.winfo_children():
        widget.destroy()
    for i, val in enumerate(input_list):
        Item(frame, val, i)

# 포커스 들어올 때
def on_focus_in(event):
    if entry.get() == '여기에 입력하세요':
        entry.delete(0, tkinter.END)
        entry.config(fg='black')

# 포커스 나갈 때
def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, '여기에 입력하세요')
        entry.config(fg='gray')

# 입력값 길이 제한
def validate_length(new_value):
    if new_value == '여기에 입력하세요':
        return True
    return len(new_value) <= 4

vcmd = (root.register(validate_length), '%P')

entry = tkinter.Entry(root, fg='gray', validate='key', validatecommand=vcmd)
entry.insert(0, '여기에 입력하세요')
entry.pack()
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

button = tkinter.Button(root, text='추가', command=add_input)
button.pack()

frame = tkinter.Frame(root)
frame.pack(fill='both', expand=True)

# 종료할 때까지 계속 실행
root.mainloop()