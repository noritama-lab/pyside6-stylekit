from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from pyside6stylekit import (
    Theme, StyledLabel, StyledButton,
    IndusMomentaryButton, IndusAlternateButton,
    IndusLamp
)
import sys


class SampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndusLamp Minimal Demo")

        layout = QVBoxLayout()

        # -------------------------
        # テーマ
        # -------------------------
        base_theme = Theme(mode="light", size="large", text_color="white")
        button_theme = Theme(primary="green", mode="dark", size="mid", text_color="white")

        title = StyledLabel("IndusLamp Minimal Demo", base_theme, bold=True)

        # -------------------------
        # ボタン
        # -------------------------
        self.enable_btn = StyledButton("Disable Buttons", button_theme)
        self.enable_btn.setCheckable(True)
        self.enable_btn.clicked.connect(self.toggle_enabled)

        self.moment_btn = IndusMomentaryButton("START", button_theme, diameter=56)
        self.alt_btn = IndusAlternateButton("RUN", button_theme, diameter=56)

        # RUN ボタンとランプを連動
        self.alt_btn.toggled.connect(self.update_lamp)

        # -------------------------
        # ランプ（中央文字のみ）
        # -------------------------
        self.lamp = IndusLamp("RUN", button_theme, diameter=54, state=False)

        # -------------------------
        # レイアウト
        # -------------------------
        layout.addWidget(title)
        layout.addSpacing(10)

        layout.addWidget(self.enable_btn)
        layout.addSpacing(20)

        layout.addWidget(self.moment_btn)
        layout.addWidget(self.alt_btn)
        layout.addWidget(self.lamp)

        self.setLayout(layout)

    # -------------------------
    # 有効/無効切り替え処理
    # -------------------------
    def toggle_enabled(self):
        disabled = self.enable_btn.isChecked()

        self.moment_btn.setEnabled(not disabled)
        self.alt_btn.setEnabled(not disabled)
        self.lamp.setEnabled(not disabled)

        self.enable_btn.setText("Enable Buttons" if disabled else "Disable Buttons")

    # -------------------------
    # RUN ボタンとランプの連動
    # -------------------------
    def update_lamp(self, checked):
        self.lamp.set_state(checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SampleWindow()
    w.resize(360, 360)
    w.show()
    sys.exit(app.exec())