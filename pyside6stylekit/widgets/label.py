# widgets/label.py
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont

class StyledLabel(QLabel):
    def __init__(self, text, theme, bold=False):
        super().__init__(text)
        weight = QFont.Bold if bold else QFont.Normal
        self.setFont(QFont(theme.font_family, theme.font_size(), weight))

        self.setStyleSheet(f"""
            QLabel {{
                color: {theme.text_color};
                background: {theme.background};
                font-family: '{theme.font_family}';
            }}
        """)