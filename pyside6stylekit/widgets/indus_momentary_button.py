# widgets/indus_momentary_button.py
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QIcon, QColor

def darken(hex_color: str, factor: float = 0.7) -> str:
    c = QColor(hex_color)
    r = int(c.red() * factor)
    g = int(c.green() * factor)
    b = int(c.blue() * factor)
    return f"#{r:02x}{g:02x}{b:02x}"

class IndusMomentaryButton(QPushButton):
    def __init__(self, text, theme, icon_path=None, diameter=48, text_color=None):
        super().__init__(text)
        self.theme = theme
        self.diameter = diameter
        self.text_color = text_color or theme.text_color

        self.setCheckable(False)
        self.setFixedSize(diameter, diameter)
        self.setFont(QFont(theme.font_family, theme.font_size()))

        if icon_path:
            self.setIcon(QIcon(icon_path))

        self.apply_style()

    def apply_style(self):
        bg = darken(self.theme.primary, 0.5)
        hover = darken(self.theme.primary, 0.6)
        pressed = self.theme.primary
        border_color = darken(self.theme.primary, 0.8)

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg};
                color: {self.text_color};
                border-radius: {self.diameter // 2}px;
                border: 2px solid {border_color};
                font-family: '{self.theme.font_family}';
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