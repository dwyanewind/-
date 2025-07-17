import socket
import subprocess
import psutil


def diagnose_network():
    """
    返回:
        - result: [(名称, 状态, IP, 网关, 网关连通性), ...]
        - internet_status: 外网连通性
    """
    result = []

    for iface, addrs in psutil.net_if_addrs().items():
        ip = ''
        gateway = ''
        status = '启用' if psutil.net_if_stats()[iface].isup else '禁用'

        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
                break

        gateways = psutil.net_if_stats()
        if iface in gateways and gateways[iface].isup and ip:
            if ip.startswith("127.") or ip == '':
                gateway = '-'
            else:
                gateway = ip.rsplit('.', 1)[0] + '.1'
        else:
            gateway = '-'

        if gateway != '-' and gateway != '0.0.0.0':
            try:
                subprocess.check_output(['ping', '-n', '1', '-w', '500', gateway],
                                        encoding='gbk', stderr=subprocess.DEVNULL)
                gw_status = '正常'
            except subprocess.CalledProcessError:
                gw_status = '异常'
        else:
            gw_status = '-'

        result.append([iface, status, ip, gateway, gw_status])

    # 外网连通性检测
    try:
        subprocess.check_output(['ping', '-n', '1', '-w', '1000', 'baidu.com'],
                                encoding='gbk', stderr=subprocess.DEVNULL)
        internet_status = "baidu.com：正常"
    except subprocess.CalledProcessError:
        internet_status = "baidu.com：异常"

    return result, internet_status
