# widgets/label.py
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont

class StyledLabel(QLabel):
    def __init__(self, text, theme, text_color=None, background_color=None):
        super().__init__(text)

        self.setFont(QFont(theme.font_family, theme.font_size()))

        # 文字色（個別指定 > theme）
        color = text_color or theme.text_color

        # 背景色（個別指定 > theme）
        bg = background_color if background_color is not None else theme.background

        self.setStyleSheet(f"""
            QLabel {{
                color: {color};
                background: {bg};
                font-family: '{theme.font_family}';
            }}
        """)