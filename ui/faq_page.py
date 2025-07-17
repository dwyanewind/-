from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QTextEdit
from modules import faq_tools


class FAQPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.faq_list = QListWidget()
        self.faq_list.addItems(faq_tools.get_faq_list())
        self.faq_list.currentRowChanged.connect(self.show_faq_answer)
        self.faq_list.setStyleSheet("font-size: 14px;")

        self.faq_answer = QTextEdit()
        self.faq_answer.setReadOnly(True)
        self.faq_answer.setStyleSheet("font-family: 微软雅黑; font-size: 13px; background-color: #FFFFFF;")

        layout.addWidget(self.faq_list, 2)
        layout.addWidget(self.faq_answer, 5)
        self.setLayout(layout)

    def show_faq_answer(self, index):
        answer = faq_tools.get_faq_answer(index)
        self.faq_answer.setText(answer)
