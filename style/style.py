app_style = """
QMainWindow { background-color: #F7F7F7; }
QListWidget { background-color: #FFFFFF; border: none; font-size: 14px; }
QListWidget::item { padding: 10px; }
QListWidget::item:selected { background-color: #E6F0FF; color: #333333; }
QPushButton {
    background-color: #4A90E2; color: white; border: none;
    padding: 8px 12px; border-radius: 5px; font-size: 14px;
}
QPushButton:hover { background-color: #357ABD; }
QPushButton:pressed { background-color: #2A5D9F; }
QTextEdit {
    border: 1px solid #DDDDDD; background-color: #FFFFFF;
    font-family: Consolas; font-size: 12px; padding: 6px;
}
QLabel#AboutLabel {
    font-size: 18px;
    color: #333333;
    font-weight: bold;
    font-family: "Microsoft YaHei";
}
QLabel { font-size: 13px; color: #555555; }
*:focus { outline: none; }
"""
