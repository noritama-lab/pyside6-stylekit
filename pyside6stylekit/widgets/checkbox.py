# widgets/checkbox.py
from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QFont

class StyledCheckBox(QCheckBox):
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
            QCheckBox {{
                color: {self.theme.text_color};
                font-family: '{self.theme.font_family}';
                spacing: {pad_h}px;
                background: {self.background if self.background is not None else self.theme.background};
            }}
            QCheckBox::indicator {{
                width: {self.theme.font_size() + 4}px;
                height: {self.theme.font_size() + 4}px;
                border: 2px solid {self.theme.border_color};
                border-radius: 3px;
                background: {self.theme.background};
            }}
            QCheckBox::indicator:checked {{
                background: {self.theme.primary};
                border: 2px solid {self.theme.primary};
            }}
            QCheckBox::indicator:hover {{
                border: 2px solid {self.theme.primary};
            }}
        """)