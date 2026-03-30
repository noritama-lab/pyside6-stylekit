# widgets/label.py
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont

class StyledLabel(QLabel):
    def __init__(self, text, theme, bold=False,
                 text_color=None, background_color=None):
        super().__init__(text)

        weight = QFont.Bold if bold else QFont.Normal
        self.setFont(QFont(theme.font_family, theme.font_size(), weight))

        # 文字色（個別指定 > theme）
        color = text_color or theme.text_color

        # 背景色（個別指定 > transparent）
        bg = background_color or "transparent"

        self.setStyleSheet(f"""
            QLabel {{
                color: {color};
                background: {bg};
                font-family: '{theme.font_family}';
            }}
        """)