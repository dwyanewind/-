from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from modules import printer_tools


class PrinterPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("打印机修复")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("遇到打印机无法打印、排队卡住时请点击此按钮。")
        self.output = QTextEdit()

        btn_fix = QPushButton("一键修复打印问题")
        btn_fix.clicked.connect(self.fix_printer)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(btn_fix)
        layout.addWidget(self.output)
        self.setLayout(layout)

    def fix_printer(self):
        self.output.setText(printer_tools.one_click_fix())
