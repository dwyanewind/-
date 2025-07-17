from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        text = (
            "软件名称：   设备诊断工具\n"
            "版本号：     V1.0.0\n"
            "开发人：   不顾\n"
            "版权所有：   © 2025\n"
            "\n"
            "本软件用于提升日常办公效率，相关功能解释与后续更新以研发部门最终发布为准。"
        )

        label = QLabel(text)
        label.setObjectName("AboutLabel")  # 关键，style里单独设置它
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setWordWrap(True)
        layout.addWidget(label)
        self.setLayout(layout)
