# widgets/progressbar.py
from PySide6.QtWidgets import QProgressBar

class StyledProgressBar(QProgressBar):
    def __init__(self, theme, min_val=0, max_val=100, value=0, background=None):
        super().__init__()
        self.theme = theme
        self.background = background
        self.setRange(min_val, max_val)
        self.setValue(value)
        self.apply_style()

    def apply_style(self):
        self.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid {self.theme.border_color};
                border-radius: 5px;
                text-align: center;
                background: {self.background if self.background is not None else self.theme.background};
                color: {self.theme.text_color};
            }}
            QProgressBar::chunk {{
                background: {self.theme.primary};
                border-radius: 3px;
            }}
        """)