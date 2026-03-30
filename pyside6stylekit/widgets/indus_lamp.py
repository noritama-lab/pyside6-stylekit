# widgets/indus_lamp.py
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class IndusLamp(QLabel):
    def __init__(self, text, theme, diameter=48,
                 state=False, text_color=None):
        super().__init__(text)

        self.theme = theme
        self.diameter = diameter
        self.state = state
        self.text_color = text_color or theme.text_color

        self.setFixedSize(diameter, diameter)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(theme.font_family, theme.font_size()))

        self.apply_style()

    # -------------------------
    # 状態変更
    # -------------------------
    def set_state(self, state: bool):
        self.state = state
        self.apply_style()

    # -------------------------
    # 色適用（丸ボタンと完全一致）
    # -------------------------
    def apply_style(self):
        if not self.isEnabled():
            bg = "#999"
            fg = "#666"
        else:
            if self.state:
                bg = self.theme.primary
            else:
                bg = self.theme.primary_dark(0.5)
            fg = self.text_color

        self.setStyleSheet(f"""
            QLabel {{
                background-color: {bg};
                color: {fg};
                border-radius: {self.diameter // 2}px;
                border: none;
                font-family: '{self.theme.font_family}';
                font-weight: bold;
            }}
        """)