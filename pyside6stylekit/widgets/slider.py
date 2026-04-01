# widgets/slider.py
from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

class StyledSlider(QSlider):
    def __init__(self, theme, orientation=Qt.Horizontal, min_val=0, max_val=100, value=0, background=None):
        super().__init__(orientation)
        self.theme = theme
        self.background = background
        self.setRange(min_val, max_val)
        self.setValue(value)
        self.apply_style()

    def apply_style(self):
        self.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                height: 8px;
                background: {self.background if self.background is not None else self.theme.border_color};
                border-radius: 4px;
            }}
            QSlider::handle:horizontal {{
                background: {self.theme.primary};
                border: 2px solid {self.theme.primary};
                width: 18px;
                height: 18px;
                border-radius: 9px;
                margin: -5px 0;
            }}
            QSlider::handle:horizontal:hover {{
                background: {self.theme.hover()};
                border: 2px solid {self.theme.hover()};
            }}
            QSlider::sub-page:horizontal {{
                background: {self.theme.primary};
                border-radius: 4px;
            }}
        """)