import webbrowser
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class DownloadPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("常用软件下载")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("一键跳转至官网下载页面，避免下载盗版或假软件。")
        layout.addWidget(title)
        layout.addWidget(desc)

        softwares = {
            'Chrome（干净舒服）': 'https://www.google.cn/chrome/',
            '微信（必备）': 'https://pc.weixin.qq.com/',
            'QQ（肌肉记忆）': 'https://im.qq.com/',
            'WPS（广告多还要钱）': 'https://www.wps.cn/',
            '360解压（将就用吧）': 'https://www.360.cn/yasuobao/',
            '办公工具（推荐）': 'http://www.wofficebox.cn/'
        }
        for name, url in softwares.items():
            btn = QPushButton(f"{name} 官网下载")
            btn.clicked.connect(lambda checked, link=url: webbrowser.open(link))
            layout.addWidget(btn)

        self.setLayout(layout)
