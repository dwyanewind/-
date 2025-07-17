import traceback
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from modules import systeminfo_tools


class SystemInfoPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("系统信息")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("列出主板、CPU、显卡、内存等基础信息，排查硬件问题时使用。")

        self.output = QTextEdit()

        btn_info = QPushButton("获取系统信息")
        btn_info.clicked.connect(self.safe_system_info)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(btn_info)
        layout.addWidget(self.output)
        self.setLayout(layout)

    def safe_system_info(self):
        try:
            self.output.setText(systeminfo_tools.get_system_info())
        except Exception as e:
            self.output.setText(f"获取失败: {e}\n{traceback.format_exc()}")
