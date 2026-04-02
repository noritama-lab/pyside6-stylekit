from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from pyside6stylekit import (Theme, StyledLabel, StyledLineEdit, StyledButton,
                             StyledCheckBox, StyledRadioButton, StyledComboBox,
                             StyledSlider, StyledProgressBar,
                             StyledTextEdit, StyledGroupBox)
import sys


class SampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6StyleKit Demo")

        layout = QVBoxLayout()

        # -------------------------
        theme = Theme(primary="blue", mode="light", size="small")

        # タイトル専用テーマ（背景透明、文字色白）
        theme_title = Theme(primary="blue", mode="light", size="large", 
                           background="transparent", text_color="white")

        # チェックボックス専用テーマ（背景透明、文字色白）
        theme_checkbox = Theme(primary="blue", mode="light", size="small",
                              background="transparent", text_color="white")

        # GroupBox専用テーマ（背景透過）
        theme_groupbox = Theme(primary="blue", mode="light", size="small", 
                               background="transparent", text_color="white")

        # タイトル
        title = StyledLabel("PySide6StyleKit Demo", theme_title)

        # -------------------------
        # 入力欄
        # -------------------------
        input_free = StyledLineEdit("Free input", theme, mode="free")
        input_numeric = StyledLineEdit("Numeric only", theme, mode="numeric")
        input_alnum = StyledLineEdit("Alphanumeric only", theme, mode="alnum")
        input_filename = StyledLineEdit("Filename OK", theme, mode="filename")
        input_numeric_range = StyledLineEdit("Range (0-120)", theme,
                                   mode="numeric_range", min_val=-10.00, max_val=120.88)

        # 新しいウィジェット
        checkbox = StyledCheckBox("CheckBox", theme_checkbox, checked=True)
        radiobutton = StyledRadioButton("RadioButton", theme_checkbox)
        combobox = StyledComboBox(theme, ["Option 1", "Option 2", "Option 3"])
        slider = StyledSlider(theme, min_val=0, max_val=100, value=50)
        progressbar = StyledProgressBar(theme, 0, 100, 75)
        textedit = StyledTextEdit(theme, "Multi-line text editor")
        groupbox = StyledGroupBox("Additional Controls", theme_groupbox)

        # グループボックス内にウィジェットを追加
        group_layout = QVBoxLayout()
        group_layout.addWidget(checkbox)
        group_layout.addWidget(radiobutton)
        groupbox.setLayout(group_layout)

        # ボタン
        button = StyledButton("Validate Input", theme)

        # -------------------------
        # レイアウトに追加
        # -------------------------
        layout.addWidget(title)
        layout.addSpacing(10)

        layout.addWidget(input_free)
        layout.addWidget(input_numeric)
        layout.addWidget(input_alnum)
        layout.addWidget(input_filename)
        layout.addWidget(input_numeric_range)

        layout.addWidget(combobox)
        layout.addWidget(slider)
        layout.addWidget(progressbar)
        layout.addWidget(textedit)
        layout.addWidget(groupbox)
        layout.addWidget(button)

        # ボタンの接続
        button.clicked.connect(lambda: self.validate(input_numeric_range))

        self.setLayout(layout)

    # -------------------------
    # バリデーション処理
    # -------------------------
    def validate(self, widget: StyledLineEdit):
        if widget.is_valid():
            widget.show_error("")   # Hide error
            print("OK:", widget.value())
        else:
            widget.show_error("Value out of range")
            print("NG")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SampleWindow()
    w.resize(500, 700)
    w.show()
    sys.exit(app.exec())