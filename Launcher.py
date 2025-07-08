# 모듈 임포트
import tkinter as tk
import requests as req
import os

# tkinter 초기 설정
root = tk.Tk()
root.title('돌림판 런처')
root.geometry('800x600')
root.resizable(False, False)

# 버전 설정
launcher_version = '1.0.0'
dollimpan_version = '1.0.1'

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
            tk.messagebox.showinfo('업데이트', '이미 최신 버전입니다.')
            return
        if latest_version != launcher_version:
            # 업데이트 파일 다운로드
            asset = next((a for a in data['assets'] if a['name'] == 'Launcher.exe'), None)
            if not asset:
                tk.messagebox.showerror('업데이트', '업데이트 파일을 찾을 수 없습니다.')
                return
            
            save_path = 'Launcher_new.exe'
            with req.get(asset['browser_download_url'], stream=True) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            tk.messagebox.showinfo('업데이트', f'최신 버전 {latest_version}을 다운로드했습니다. 프로그램을 종료하고 새 버전을 실행하세요.')
            root.quit()
    except Exception as e:
        tk.messagebox.showerror('업데이트 오류', f'업데이트 중 오류가 발생했습니다: {e}')

# 돌림판 업데이트
def dollimpan_update():
    try:
        # 깃허브 API를 통해 최신 버전 확인
        api_url = 'https://api.github.com/repos/haeengin/dollimpan/releases/latest'
        response = req.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        latest_version = data['tag_name'].lstrip('v')
        if latest_version == dollimpan_version:
            tk.messagebox.showinfo('업데이트', '이미 최신 버전입니다.')
            return
        if latest_version != dollimpan_version:
            # 업데이트 파일 다운로드
            asset = next((a for a in data['assets'] if a['name'] == 'Dollimpan.exe'), None)
            if not asset:
                tk.messagebox.showerror('업데이트', '업데이트 파일을 찾을 수 없습니다.')
                return
            
            save_path = 'Dollimpan_new.exe'
            with req.get(asset['browser_download_url'], stream=True) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            # 기존 파일 삭제 및 이름 변경
            try:
                if os.path.exists('Dollimpan.exe'):
                    os.remove('Dollimpan.exe')
                os.rename('Dollimpan_new.exe', 'Dollimpan.exe')
                tk.messagebox.showinfo('업데이트', f'최신 버전 {latest_version}으로 교체되었습니다. 프로그램을 종료하고 새 버전을 실행하세요.')
            except Exception as file_err:
                tk.messagebox.showerror('업데이트 오류', f'파일 교체 중 오류가 발생했습니다: {file_err}')
            root.quit()
    except Exception as e:
        tk.messagebox.showerror('업데이트 오류', f'업데이트 중 오류가 발생했습니다: {e}')