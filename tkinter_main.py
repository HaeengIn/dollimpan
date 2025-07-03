# 모듈 임포트
import tkinter
import random
import webbrowser

# tkinter 초기 설정
root = tkinter.Tk()
root.title('Dol Lim Pan')
root.geometry('800x600')
root.resizable(False, False)

input_list = []
placeholder = '여기에 입력하세요. (최대 4자)'

# 객체 클래스 정의
class Item:
    def __init__(self, master, value, index):
        self.value = value
        self.button = tkinter.Button(master, text=value, command=lambda: self.delete(index))
        self.button.pack(pady=(10))

    def delete(self, index):
        del input_list[index]
        render_objects()

# 리스트에 입력값 추가
def add_input():
    value = entry.get()
    if value != placeholder and value != '':
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
    if entry.get() == placeholder:
        entry.delete(0, tkinter.END)
        entry.config(fg='black')

# 포커스 나갈 때
def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='gray')

# 입력값 길이 제한
def validate_length(new_value):
    if new_value == placeholder:
        return True
    return len(new_value) <= 4

# esc 누르면 포커스 취소
def on_escape(event):
    root.focus_set()

# / 누르면 자동 포커스
def focus_entry(event):
    entry.focus_set()
    
# 추첨
def draw_random():
    for widget in result_frame.winfo_children():
        widget.destroy()

    if input_list:
        winner = random.choice(input_list)
        winner_btn = tkinter.Button(result_frame, text=f'{winner}')
        winner_btn.pack(pady=(10))
    else:
        empty_list = tkinter.Label(result_frame, text='리스트가 비어있습니다.', fg='red')
        empty_list.pack(pady=(10))

# 도움말 열기
def open_help():
    webbrowser.open_new_tab("https://haeengin.kro.kr/dollimpan_help")

vcmd = (root.register(validate_length), '%P')

entry = tkinter.Entry(root, fg='gray', validate='key', validatecommand=vcmd, width=25, font=('맑은 고딕', 10))
entry.insert(0, placeholder)
entry.pack(pady=(30))
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.bind("<Escape>", on_escape)
entry.bind("<Return>", lambda event: add_input())
root.bind("/", focus_entry)

button = tkinter.Button(root, text='추가', command=add_input)
button.pack()

frame = tkinter.Frame(root)
frame.pack()

draw_button = tkinter.Button(root, text='추첨', command=draw_random)
draw_button.pack(pady=(10))

result_frame = tkinter.Frame(root)
result_frame.pack()

help_button = tkinter.Button(root, text='도움말', command=open_help)
help_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # 오른쪽 위에 여백 주기

# 종료할 때까지 계속 실행
root.mainloop()