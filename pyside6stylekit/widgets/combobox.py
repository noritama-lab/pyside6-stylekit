# widgets/combobox.py
from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QFont

class StyledComboBox(QComboBox):
    def __init__(self, theme, items=None, background=None):
        super().__init__()
        self.theme = theme
        self.background = background
        self.setFont(QFont(theme.font_family, theme.font_size()))
        if items:
            self.addItems(items)
        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()

        self.setStyleSheet(f"""
            QComboBox {{
                padding: {pad_v}px {pad_h}px;
                border: 2px solid {self.theme.border_color};
                border-radius: 6px;
                background: {self.background if self.background is not None else self.theme.background};
                color: {self.theme.text_color};
                font-family: '{self.theme.font_family}';
            }}
            QComboBox:focus {{
                border: 2px solid {self.theme.primary};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QComboBox::down-arrow {{
                image: url(down_arrow.png);  /* Placeholder for arrow icon */
                width: 12px;
                height: 12px;
            }}
            QComboBox QAbstractItemView {{
                border: 2px solid {self.theme.border_color};
                background: {self.theme.background};
                color: {self.theme.text_color};
                selection-background-color: {self.theme.primary};
            }}
        """)