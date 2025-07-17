from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QSizePolicy
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QEvent
from modules import ai_tools_core


class AIChatWorker(QThread):
    text_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, user_message):
        super().__init__()
        self.user_message = user_message

    def run(self):
        for new_text in ai_tools_core.send_message_streaming(
                ai_tools_core.assistant_id, ai_tools_core.access_token, self.user_message):
            self.text_signal.emit(new_text)
        self.finish_signal.emit()


class AIPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("AI 聊天助手")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")

        # 历史对话框
        self.ai_history = QTextEdit()
        self.ai_history.setReadOnly(True)
        self.ai_history.setStyleSheet("font-family: 微软雅黑; font-size: 13px; background-color: #FFFFFF;")
        self.ai_history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 输入框
        self.ai_input = QTextEdit()
        self.ai_input.setFixedHeight(80)
        self.ai_input.setPlaceholderText("请输入你的问题，按回车发送")
        self.ai_input.installEventFilter(self)

        btn_send = QPushButton("发送给 AI")
        btn_send.clicked.connect(self.send_to_ai_stream)

        layout.addWidget(title)
        layout.addWidget(QLabel("对话记录："))
        layout.addWidget(self.ai_history, stretch=4)
        layout.addWidget(QLabel("提问内容："))
        layout.addWidget(self.ai_input, stretch=1)
        layout.addWidget(btn_send)

        self.setLayout(layout)
        self.ai_input.setFocus()

    def eventFilter(self, obj, event):
        if obj == self.ai_input and event.type() == QEvent.KeyPress:
            key = event.key()
            modifiers = event.modifiers()

            is_enter = key in (Qt.Key_Return, Qt.Key_Enter)

            if is_enter and (modifiers & Qt.ControlModifier):
                # Ctrl + Enter 手动插入换行
                cursor = self.ai_input.textCursor()
                cursor.insertText('\n')
                return True  # 防止传递
            elif is_enter and not (modifiers & Qt.ControlModifier):
                # 直接 Enter 发送
                self.send_to_ai_stream()
                return True
        return super().eventFilter(obj, event)

    def send_to_ai_stream(self):
        user_message = self.ai_input.toPlainText().strip()
        if not user_message:
            QMessageBox.warning(self, "提示", "请输入内容。")
            return

        self.ai_history.append(f"👤 你：{user_message}")
        self.ai_input.clear()

        self.ai_response_buffer = ""
        self.ai_history.append("🤖 AI：")

        self.worker = AIChatWorker(user_message)
        self.worker.text_signal.connect(self.append_ai_response)
        self.worker.finish_signal.connect(self.finish_ai_response)
        self.worker.start()

    def append_ai_response(self, text):
        self.ai_response_buffer += text
        cursor = self.ai_history.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.ai_history.setTextCursor(cursor)
        self.ai_history.ensureCursorVisible()

    def finish_ai_response(self):
        self.ai_history.append("")  # 换行美观
        self.ai_history.moveCursor(QTextCursor.End)
