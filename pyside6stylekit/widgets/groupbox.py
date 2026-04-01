# widgets/groupbox.py
from PySide6.QtWidgets import QGroupBox
from PySide6.QtGui import QFontMetrics, QFont

class StyledGroupBox(QGroupBox):
    def __init__(self, title, theme, background=None):
        super().__init__(title)
        self.theme = theme
        self.background = background if background is not None else theme.background

        font = QFont(theme.font_family, theme.font_size())
        self.setFont(font)

        # タイトル文字の高さを取得
        fm = QFontMetrics(font)
        self.title_height = fm.height()

        self.apply_style()

    def apply_style(self):
        pad_v, pad_h = self.theme.padding()

        # タイトル高さの半分を margin-top に設定
        margin_top = int(self.title_height / 2)

        self.setStyleSheet(f"""
            QGroupBox {{
                font-family: '{self.theme.font_family}';
                border: 2px solid {self.theme.border_color};
                border-radius: 5px;
                margin-top: {margin_top}px;
                background: {self.background};
                color: {self.theme.text_color};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: {pad_h}px;
                padding: 0 {pad_h}px;
                color: {self.theme.text_color};
            }}
        """)