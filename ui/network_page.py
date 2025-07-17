from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from modules import network_tools


class NetworkPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("网络排查")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding-bottom: 5px;")
        desc = QLabel("自动检测本地网络和外网连接，定位问题。")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["名称", "状态", "IP地址", "网关", "网关连通性"])
        self.table.horizontalHeader().setStretchLastSection(True)

        self.internet_status_label = QLabel("外网连通性：未知")

        btn_diagnose = QPushButton("一键网络诊断")
        btn_diagnose.clicked.connect(self.run_network_diagnose)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(btn_diagnose)
        layout.addWidget(self.table)
        layout.addWidget(self.internet_status_label)

        self.setLayout(layout)

    def run_network_diagnose(self):
        data, internet_status = network_tools.diagnose_network()
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        self.internet_status_label.setText("外网连通性：" + internet_status)
