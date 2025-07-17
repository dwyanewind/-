from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from modules import software_tools


class SoftwarePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("软件管理")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("打开 Windows 应用和功能，进行软件卸载管理。")

        btn_open_apps = QPushButton("打开应用和功能设置")
        btn_open_apps.clicked.connect(software_tools.open_windows_apps_panel)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(btn_open_apps)
        self.setLayout(layout)
