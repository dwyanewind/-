# modules/software_tools.py
import subprocess
import sys
import os
import winreg

def open_windows_apps_panel():
    if sys.platform == "win32":
        subprocess.Popen('start ms-settings:appsfeatures',
                         shell=True,
                         creationflags=subprocess.CREATE_NO_WINDOW)

# 启动文件夹操作
STARTUP_PATH = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')

def list_startup_folder():
    return os.listdir(STARTUP_PATH)

def delete_startup_file(filename):
    filepath = os.path.join(STARTUP_PATH, filename)
    if os.path.exists(filepath):
        os.remove(filepath)

# 注册表启动项
RUN_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def list_run_keys(root=winreg.HKEY_CURRENT_USER):
    key = winreg.OpenKey(root, RUN_PATH)
    items = []
    try:
        i = 0
        while True:
            name, value, _ = winreg.EnumValue(key, i)
            items.append((name, value))
            i += 1
    except OSError:
        pass
    return items

def delete_run_key(name, root=winreg.HKEY_CURRENT_USER):
    with winreg.OpenKey(root, RUN_PATH, 0, winreg.KEY_SET_VALUE) as key:
        winreg.DeleteValue(key, name)

# 任务计划操作
def list_task_schedulers():
    result = subprocess.getoutput('schtasks /query /fo LIST /v')
    return result

def disable_task(taskname):
    subprocess.Popen(f'schtasks /Change /TN "{taskname}" /Disable',
                     shell=True,
                     creationflags=subprocess.CREATE_NO_WINDOW)
