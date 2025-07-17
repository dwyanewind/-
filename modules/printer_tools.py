import os
import subprocess
import ctypes


def one_click_fix():
    output = []

    def run_cmd(command):
        try:
            result = subprocess.check_output(command, shell=True, encoding='gbk', errors='ignore')
            return result.strip()
        except Exception as e:
            return str(e)

    # 检查是否管理员权限
    if not ctypes.windll.shell32.IsUserAnAdmin():
        return "请使用管理员权限运行此工具！"

    output.append("【打印机一键修复】开始：\n")

    output.append("1、 停止打印服务...")
    output.append(run_cmd('net stop spooler'))

    output.append("\n2、 清理残留打印任务...")
    spool_path = r"C:\Windows\System32\spool\PRINTERS"
    try:
        for filename in os.listdir(spool_path):
            filepath = os.path.join(spool_path, filename)
            os.remove(filepath)
        output.append("✅ 残留任务已清理")
    except Exception as e:
        output.append(f"⚠ 清理失败或无残留任务：{e}")

    output.append("\n3、 重启打印服务...")
    output.append(run_cmd('net start spooler'))

    output.append("\n4、 修复完成 ✅")
    output.append("\n✅ 修复完成！如仍无法打印，请重新插拔打印机或联系研发部门。")

    return "\n".join(output)
