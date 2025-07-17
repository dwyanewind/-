from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from modules import filetype_tools


class FiletypePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("默认应用设置")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("用于设置默认打开软件，比如 PDF、浏览器、图片查看器等。")

        btn_defaultapps = QPushButton("打开 Windows 默认应用设置")
        btn_defaultapps.clicked.connect(filetype_tools.open_windows_default_apps)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(btn_defaultapps)
        self.setLayout(layout)
