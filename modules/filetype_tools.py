import subprocess
import sys

def open_windows_default_apps():
    if sys.platform == "win32":
        subprocess.Popen('start ms-settings:defaultapps',
                         shell=True,
                         creationflags=subprocess.CREATE_NO_WINDOW)
