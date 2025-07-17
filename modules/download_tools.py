import webbrowser

def open_download_site(name):
    sites = {
        'chrome': 'https://www.google.cn/chrome/',
        'wechat': 'https://pc.weixin.qq.com/',
        'qq': 'https://im.qq.com/',
        'wps': 'https://www.wps.cn/',
        '360zip': 'https://www.360.cn/weishi/',
        '办公工具': 'http://www.wofficebox.cn/'
    }
    if name in sites:
        webbrowser.open(sites[name])
