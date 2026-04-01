# widgets/textedit.py
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QFont

class StyledTextEdit(QTextEdit):
    def __init__(self, theme, placeholder="", background=None):
        super().__init__()
        self.theme = theme
        self.background = background
        self.setPlaceholderText(placeholder)
        self.setFont(QFont(theme.font_family, theme.font_size()))
        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()

        self.setStyleSheet(f"""
            QTextEdit {{
                padding: {pad_v}px {pad_h}px;
                border: 2px solid {self.theme.border_color};
                border-radius: 6px;
                background: {self.background if self.background is not None else self.theme.background};
                color: {self.theme.text_color};
                font-family: '{self.theme.font_family}';
            }}
            QTextEdit:focus {{
                border: 2px solid {self.theme.primary};
            }}
        """)