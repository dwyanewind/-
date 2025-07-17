import os
import datetime
import wmi
import psutil
import platform

LOG_PATH = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

LOG_FILE = os.path.join(LOG_PATH, 'systeminfo_tools.log')

def log(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


def get_system_info():
    try:
        c = wmi.WMI()

        # 主板
        boards = c.Win32_BaseBoard()
        board_info = boards[0].Product.strip() if boards else "未知"

        # CPU
        cpus = c.Win32_Processor()
        cpu_info = cpus[0].Name.strip() if cpus else "未知"

        # 显卡
        gpus = c.Win32_VideoController()
        gpu_info = gpus[0].Name.strip() if gpus else "未知"

        # 内存
        mem_total = round(psutil.virtual_memory().total / (1024 ** 3), 2)

        # 系统
        system_info = platform.platform()

        result = (
            f"主板: {board_info}\n"
            f"CPU: {cpu_info}\n"
            f"显卡: {gpu_info}\n"
            f"内存: {mem_total} GB\n"
            f"系统: {system_info}"
        )
        log("查询系统信息")
        return result
    except Exception as e:
        log(f"查询系统信息失败: {e}")
        return f"获取失败: {e}"
