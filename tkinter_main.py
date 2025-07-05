# 모듈 임포트
import tkinter as tk
import random as ran
import webbrowser as web

# tkinter 초기 설정
root = tk.Tk()
root.title('Dol Lim Pan')
root.geometry('800x600')
root.resizable(False, False)

input_list = []
placeholder = '여기에 입력하세요. (최대 4자)'

# 객체 클래스 정의
class Item:
    def __init__(self, master, value, index):
        self.value = value
        self.button = tk.Button(master, text=value, command=lambda: self.delete(index))
        self.button.pack(pady=(10))

    def delete(self, index):
        del input_list[index]
        render_objects()

# 리스트에 입력값 추가
def add_input():
    value = entry.get()
    if value != placeholder and value != '':
        input_list.append(value)
        entry.delete(0, tk.END) # 입력창 비우기
        render_objects()

# 리스트 객체 렌더링
def render_objects():
    for widget in frame.winfo_children():
        widget.destroy()
    if input_list:
        frame.pack_configure(pady=(10))  # 리스트가 있을 때만 여백
        for i, val in enumerate(input_list):
            Item(frame, val, i)
    else:
        frame.pack_configure(pady=(0))   # 리스트가 없으면 여백 없음

# 포커스 들어올 때
def on_focus_in(event):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
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
        winner = ran.choice(input_list)
        winner_btn = tk.Button(result_frame, text=f'{winner}')
        winner_btn.pack(pady=(10))
    else:
        empty_list = tk.Label(result_frame, text='리스트가 비어있습니다.', fg='red')
        empty_list.pack(pady=(10))

    reset_btn = tk.Button(result_frame, text='재설정', command=reset_all)
    reset_btn.pack(pady=(10))

    
# 전체 초기화
def reset_all():
    global input_list
    input_list.clear()
    entry.delete(0, tk.END)
    entry.insert(0, placeholder)
    entry.config(fg='gray')
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

# 도움말 열기
def open_help():
    web.open_new_tab("https://haeengin.kro.kr/dollimpan_help")

# 입력값 길이 제한
vcmd = (root.register(validate_length), '%P')

entry = tk.Entry(root, fg='gray', validate='key', validatecommand=vcmd, width=25, font=('맑은 고딕', 10)) # 입력창 생성
entry.insert(0, placeholder) # 플레이스홀더 설정
entry.pack(pady=(30)) 
entry.bind("<FocusIn>", on_focus_in) # 포커스 들어올 때
entry.bind("<FocusOut>", on_focus_out) # 포커스 나갈 때
entry.bind("<Escape>", on_escape) # esc 누르면 포커스 취소
entry.bind("<Return>", lambda event: add_input()) # 엔터키로 입력값 추가
root.bind("/", focus_entry) # / 누르면 자동 포커스

button = tk.Button(root, text='추가', command=add_input) # 입력값 추가 버튼
button.pack()

frame = tk.Frame(root) # 입력값 리스트를 담을 프레임
frame.pack(pady=(0))

draw_button = tk.Button(root, text='추첨', command=draw_random) # 추첨 버튼
draw_button.pack(pady=(5))

result_frame = tk.Frame(root) # 추첨 결과를 담을 프레임
result_frame.pack()

help_button = tk.Button(root, text='도움말', command=open_help) # 도움말 버튼
help_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # 우측 상단 정렬

# 종료할 때까지 계속 실행
root.mainloop()