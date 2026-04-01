# widgets/lineedit.py
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QToolTip
from PySide6.QtGui import QFont, QRegularExpressionValidator, QIntValidator, QDoubleValidator
from PySide6.QtCore import QRegularExpression

class StyledLineEdit(QWidget):
    def __init__(self, placeholder, theme, mode="free",
                 min_val=None, max_val=None, background=None):
        super().__init__()

        self.theme = theme
        self.mode = mode
        self.min_val = min_val
        self.max_val = max_val
        self.background = background

        self.edit = QLineEdit()
        self.error_label = QLabel(" ")
        self.error_label.setFixedHeight(14)
        self.error_label.setStyleSheet("color: transparent; font-size: 11px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.edit)
        layout.addWidget(self.error_label)

        self.edit.setPlaceholderText(placeholder)
        self.edit.setFont(QFont(theme.font_family, theme.font_size()))

        self.apply_style()
        self.apply_validator(mode, min_val, max_val)

    def apply_style(self, error=False):
        pad_v, pad_h = self.theme.padding()
        border_color = "red" if error else self.theme.border_color

        self.edit.setStyleSheet(f"""
            QLineEdit {{
                padding: {pad_v}px {pad_h}px;
                border: 2px solid {border_color};
                border-radius: 6px;
                background: {self.background if self.background is not None else self.theme.background};
                color: {self.theme.text_color};
                font-family: '{self.theme.font_family}';
            }}
            QLineEdit:focus {{
                border: 2px solid {self.theme.primary};
            }}
        """)

    def apply_validator(self, mode, min_val, max_val):
        if mode == "free":
            return

        if mode == "numeric":
            regex = QRegularExpression(r"^[0-9]+$")
            self.edit.setValidator(QRegularExpressionValidator(regex))
            return

        if mode == "numeric_range":
            self._apply_numeric_range(min_val, max_val)
            return

        if mode == "alnum":
            regex = QRegularExpression(r"^[A-Za-z0-9]+$")
            self.edit.setValidator(QRegularExpressionValidator(regex))
            return

        if mode == "filename":
            regex = QRegularExpression(r'^[^\\/:*?"<>|]+$')
            self.edit.setValidator(QRegularExpressionValidator(regex))
            return

        raise ValueError(f"Unknown mode: {mode}")

    def _apply_numeric_range(self, min_val, max_val):
        if min_val is None or max_val is None:
            raise ValueError("numeric_range requires min_val and max_val")

        is_int = isinstance(min_val, int) and isinstance(max_val, int)

        if is_int:
            validator = QIntValidator(min_val, max_val)
        else:
            decimals = max(self._decimal_places(min_val),
                           self._decimal_places(max_val))
            validator = QDoubleValidator(min_val, max_val, decimals)
            validator.setNotation(QDoubleValidator.StandardNotation)

        self.edit.setValidator(validator)

    def _decimal_places(self, value):
        s = str(value)
        return len(s.split(".")[1]) if "." in s else 0

    def value(self):
        try:
            return float(self.edit.text())
        except ValueError:
            return None

    def is_valid(self):
        if self.mode != "numeric_range":
            return True

        v = self.value()
        if v is None:
            return False

        return self.min_val <= v <= self.max_val

    def show_error(self, message=None):
        if message is None:
            self.error_label.setText(" ")
            self.error_label.setStyleSheet("color: transparent; font-size: 11px;")
            self.apply_style(error=True)
            return

        if message == "":
            self.error_label.setText(" ")
            self.error_label.setStyleSheet("color: transparent; font-size: 11px;")
            self.apply_style(error=False)
            return

        QToolTip.showText(self.edit.mapToGlobal(self.edit.rect().bottomLeft()), message)

        self.error_label.setText(" ")
        self.error_label.setStyleSheet("color: transparent; font-size: 11px;")
        self.apply_style(error=True)