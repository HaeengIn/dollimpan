# 모듈 임포트
import tkinter as tk
import requests as req
import os
from tkinter import messagebox
import win32api as win32

# tkinter 초기 설정
root = tk.Tk()
root.title('돌림판 런처')
root.geometry('800x600')
root.resizable(False, False)

# 돌림판 실행
def run_dollimpan():
    try:
        if os.path.exists('Dollimpan.exe'):
            os.startfile('Dollimpan.exe')
        else:
            messagebox.showerror('오류', '돌림판 실행 파일이 존재하지 않습니다.')
    except Exception as e:
        messagebox.showerror('오류', f'돌림판 실행 중 오류가 발생했습니다: {e}')

# 돌림판 버전 읽기
def get_installed_dollimpan_version():
    try:
        info = win32.GetFileVersionInfo('Dollimpan.exe', '\\')
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = f"{win32.HIWORD(ms)}.{win32.LOWORD(ms)}.{win32.HIWORD(ls)}.{win32.LOWORD(ls)}"
        return version
    except Exception:
        return '0.0'
    
# 런처 버전 읽기
def get_installed_launcher_version():
    try:
        info = win32.GetFileVersionInfo('Launcher.exe', '\\')
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = f"{win32.HIWORD(ms)}.{win32.LOWORD(ms)}.{win32.HIWORD(ls)}.{win32.LOWORD(ls)}"
        return version
    except Exception:
        return '0.0'

dollimpan_version = get_installed_dollimpan_version()
launcher_version = get_installed_launcher_version()

# 런처 업데이트
def launcher_update():
    try:
        # 깃허브 API를 통해 최신 버전 확인
        api_url = 'https://api.github.com/repos/haeengin/dollimpan/releases/latest'
        response = req.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        latest_version = data['tag_name'].lstrip('v')
        if latest_version == launcher_version:
            messagebox.showinfo('업데이트', '이미 최신 버전입니다.')
            return
        if latest_version != launcher_version:
            # 업데이트 파일 다운로드
            asset = next((a for a in data['assets'] if a['name'] == 'Launcher.exe'), None)
            if not asset:
                messagebox.showerror('업데이트', '업데이트 파일을 찾을 수 없습니다.')
                return
            
            launcher_new = f'Launcher-{latest_version}.exe'
            with req.get(asset['browser_download_url'], stream=True) as r:
                r.raise_for_status()
                with open(launcher_new, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            messagebox.showinfo('업데이트', f'최신 버전 {latest_version}을 다운로드했습니다. 프로그램을 종료하고 새 버전을 실행하세요.')
            root.quit()
    except Exception as e:
        messagebox.showerror('업데이트 오류', f'업데이트 중 오류가 발생했습니다: {e}')

# 돌림판 업데이트
def dollimpan_update():
    try:
        api_url = 'https://api.github.com/repos/haeengin/dollimpan/releases/latest'
        response = req.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        latest_version = data['tag_name'].lstrip('v')
        if latest_version == dollimpan_version:
            messagebox.showinfo('업데이트', '이미 최신 버전입니다.')
            return
        if latest_version != dollimpan_version:
            asset = next((a for a in data['assets'] if a['name'] == 'Dollimpan.exe'), None)
            if not asset:
                messagebox.showerror('업데이트', '업데이트 파일을 찾을 수 없습니다.')
                return
            
            dollimpan_new = 'Dollimpan_new.exe'
            with req.get(asset['browser_download_url'], stream=True) as r:
                r.raise_for_status()
                with open(dollimpan_new, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # 기존 파일 삭제 및 이름 변경
            try:
                if os.path.exists('Dollimpan.exe'):
                    os.remove('Dollimpan.exe')
                os.rename('Dollimpan_new.exe', 'Dollimpan.exe')
                with open('Dollimpan.version', 'w') as f:
                    f.write(latest_version)
                messagebox.showinfo('업데이트', f'최신 버전 {latest_version}으로 교체되었습니다. 프로그램을 종료하고 새 버전을 실행하세요.')
            except Exception as file_err:
                messagebox.showerror('업데이트 오류', f'파일 교체 중 오류가 발생했습니다: {file_err}')
            root.quit()
    except Exception as e:
        messagebox.showerror('업데이트 오류', f'업데이트 중 오류가 발생했습니다: {e}')

# 버튼 생성
launcher_version_label = tk.Label(root, text=f'런처 버전: {launcher_version}', font=('Arial', 16))
launcher_version_label.pack(pady=10)
launcher_update_button = tk.Button(root, text='런처 업데이트', command=launcher_update)
launcher_update_button.pack(pady=10)
dollimpan_version_label = tk.Label(root, text=f'돌림판 버전: {dollimpan_version}', font=('Arial', 16))
dollimpan_version_label.pack(pady=10)
dollimpan_update_button = tk.Button(root, text='돌림판 업데이트', command=dollimpan_update)
dollimpan_update_button.pack(pady=10)
run_button = tk.Button(root, text='돌림판 실행', command=run_dollimpan)
run_button.pack(pady=10)

# 프로그램 시작
root.mainloop()