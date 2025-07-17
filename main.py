import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QListWidget, QStackedWidget, QWidget
from style.style import app_style
from ui.network_page import NetworkPage
from ui.printer_page import PrinterPage
from ui.download_page import DownloadPage
from ui.filetype_page import FiletypePage
from ui.systeminfo_page import SystemInfoPage
from ui.software_page import SoftwarePage
from ui.faq_page import FAQPage
from ui.ai_page import AIPage
from ui.more_page import MorePage
from ui.about_page import AboutPage
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设备诊断工具1.0")
        self.resize(900, 550)
        self.setStyleSheet(app_style)

        main_layout = QHBoxLayout()
        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(160)
        self.nav_list.addItems([
            "网络排查", "打印修复", "软件下载",
            "默认应用设置", "系统信息", "软件管理",
            "自助指引", "AI 聊天助手", "更多功能", "关于"
        ])
        self.nav_list.currentRowChanged.connect(self.display_page)

        self.stack = QStackedWidget()
        self.stack.addWidget(NetworkPage())
        self.stack.addWidget(PrinterPage())
        self.stack.addWidget(DownloadPage())
        self.stack.addWidget(FiletypePage())
        self.stack.addWidget(SystemInfoPage())
        self.stack.addWidget(SoftwarePage())
        self.stack.addWidget(FAQPage())
        self.stack.addWidget(AIPage())
        self.stack.addWidget(MorePage())
        self.stack.addWidget(AboutPage())
        self.setWindowIcon(QIcon("./style/icon.ico"))

        main_layout.addWidget(self.nav_list)
        main_layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def display_page(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
