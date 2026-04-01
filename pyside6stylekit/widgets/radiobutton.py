# widgets/radiobutton.py
from PySide6.QtWidgets import QRadioButton
from PySide6.QtGui import QFont

class StyledRadioButton(QRadioButton):
    def __init__(self, text, theme, checked=False, background=None):
        super().__init__(text)
        self.theme = theme
        self.background = background
        self.setChecked(checked)
        self.setFont(QFont(theme.font_family, theme.font_size()))
        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()

        self.setStyleSheet(f"""
            QRadioButton {{
                color: {self.theme.text_color};
                font-family: '{self.theme.font_family}';
                spacing: {pad_h}px;
                background: {self.background if self.background is not None else self.theme.background};
            }}
            QRadioButton::indicator {{
                width: {self.theme.font_size() + 4}px;
                height: {self.theme.font_size() + 4}px;
                border: 2px solid {self.theme.border_color};
                border-radius: {self.theme.font_size() // 2 + 2}px;
                background: {self.theme.background};
            }}
            QRadioButton::indicator:checked {{
                background: {self.theme.primary};
                border: 2px solid {self.theme.primary};
            }}
            QRadioButton::indicator:hover {{
                border: 2px solid {self.theme.primary};
            }}
        """)