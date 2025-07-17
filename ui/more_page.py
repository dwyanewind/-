from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
class MorePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        text = (
            "敬请\n"
            "\n"
            "期待！"
        )

        label = QLabel(text)
        label.setAlignment(Qt.AlignLeft)


        label = QLabel(text)
        label.setObjectName("AboutLabel")  # 关键，style里单独设置它
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setWordWrap(True)
        layout.addWidget(label)
        self.setLayout(layout)