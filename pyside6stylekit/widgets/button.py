# widgets/button.py
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QIcon

class StyledButton(QPushButton):
    def __init__(self, text, theme, icon_path=None):
        super().__init__(text)
        self.theme = theme
        self.setFont(QFont(theme.font_family, theme.font_size()))

        if icon_path:
            self.setIcon(QIcon(icon_path))

        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.theme.primary};
                color: {self.theme.text_color};
                padding: {pad_v}px {pad_h}px;
                border-radius: 6px;
                font-family: '{self.theme.font_family}';
            }}
            QPushButton:hover {{
                background-color: {self.theme.hover()};
            }}
            QPushButton:pressed {{
                background-color: {self.theme.pressed()};
            }}
        """)