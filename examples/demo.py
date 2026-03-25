from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from pyside6stylekit import Theme, StyledLabel, StyledLineEdit, StyledButton
import sys


class SampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StyleKit Demo")

        layout = QVBoxLayout()

        # -------------------------
        # テーマ設定（Light / Dark）
        # -------------------------
        theme = Theme(
            primary="blue",
            mode="light",        # ← dark にするとダークテーマ
            size="mid"
        )

        # タイトル（別テーマで強調）
        title = StyledLabel(
            "StyleKit デモ",
            Theme(primary="blue", mode="dark", size="large"),
            bold=True
        )

        # -------------------------
        # 入力欄
        # -------------------------
        input_free = StyledLineEdit("自由入力", theme, mode="free")
        input_numeric = StyledLineEdit("数値のみ", theme, mode="numeric")
        input_alnum = StyledLineEdit("英数字のみ", theme, mode="alnum")
        input_filename = StyledLineEdit("ファイル名OK", theme, mode="filename")
        input_numeric_range = StyledLineEdit("入力制限（0〜120）", theme,
                                   mode="numeric_range", min_val=0, max_val=120)

        # -------------------------
        # ボタン
        # -------------------------
        button = StyledButton("送信", theme)
        button.clicked.connect(lambda: self.validate(input_numeric_range))

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

        layout.addSpacing(10)
        layout.addWidget(button)

        self.setLayout(layout)

    # -------------------------
    # バリデーション処理
    # -------------------------
    def validate(self, widget: StyledLineEdit):
        if widget.is_valid():
            widget.show_error("")   # エラー非表示
            print("OK:", widget.value())
        else:
            widget.show_error("範囲外の値です")
            print("NG")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SampleWindow()
    w.resize(420, 380)
    w.show()
    sys.exit(app.exec())