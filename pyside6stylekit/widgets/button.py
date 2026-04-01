# widgets/button.py
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QIcon

class StyledButton(QPushButton):
    def __init__(self, text, theme, icon_path=None, text_color=None):
        super().__init__(text)
        self.theme = theme
        self.text_color = text_color or theme.text_color

        self.setFont(QFont(theme.font_family, theme.font_size()))

        if icon_path:
            self.setIcon(QIcon(icon_path))

        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()

        bg = self.theme.primary
        hover = self.theme.hover()
        pressed = self.theme.pressed()

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg};
                color: {self.text_color};
                padding: {pad_v}px {pad_h}px;
                border-radius: 6px;
                font-family: '{self.theme.font_family}';
                border: none;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
            QPushButton:pressed {{
                background-color: {pressed};
            }}
            QPushButton:disabled {{
                background-color: #999;
                color: #666;
            }}
        """)