# widgets/lineedit.py
from PySide6.QtWidgets import QLineEdit, QToolTip
from PySide6.QtGui import QFont, QRegularExpressionValidator, QIntValidator, QDoubleValidator
from PySide6.QtCore import QRegularExpression

class StyledLineEdit(QLineEdit):
    def __init__(self, placeholder, theme, mode="free",
                 min_val=None, max_val=None, background=None):
        super().__init__()

        self.theme = theme
        self.mode = mode
        self.min_val = min_val
        self.max_val = max_val
        self.background = background
        self._numeric_range_is_int = False
        self._last_valid_text = ""

        self.setPlaceholderText(placeholder)
        self.setFont(QFont(theme.font_family, theme.font_size()))

        self.apply_style()
        self.apply_validator(mode, min_val, max_val)

    def apply_style(self, error=False):
        pad_v, pad_h = self.theme.padding()
        border_color = "red" if error else self.theme.border_color

        self.setStyleSheet(f"""
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
            self.setValidator(QRegularExpressionValidator(regex))
            return

        if mode == "numeric_range":
            self._apply_numeric_range(min_val, max_val)
            return

        if mode == "alnum":
            regex = QRegularExpression(r"^[A-Za-z0-9]+$")
            self.setValidator(QRegularExpressionValidator(regex))
            return

        if mode == "filename":
            regex = QRegularExpression(r'^[^\\/:*?"<>|]+$')
            self.setValidator(QRegularExpressionValidator(regex))
            return

        raise ValueError(f"Unknown mode: {mode}")

    def _apply_numeric_range(self, min_val, max_val):
        if min_val is None or max_val is None:
            raise ValueError("numeric_range requires min_val and max_val")

        is_int = isinstance(min_val, int) and isinstance(max_val, int)
        self._numeric_range_is_int = is_int

        if is_int:
            validator = QIntValidator(min_val, max_val)
        else:
            decimals = max(self._decimal_places(min_val),
                           self._decimal_places(max_val))
            validator = QDoubleValidator(min_val, max_val, decimals)
            validator.setNotation(QDoubleValidator.StandardNotation)

        self.setValidator(validator)
        self.textEdited.connect(self._enforce_numeric_range)

    def _decimal_places(self, value):
        s = str(value)
        return len(s.split(".")[1]) if "." in s else 0

    def _enforce_numeric_range(self, text):
        if text == "":
            self._last_valid_text = ""
            return

        if text in {"-", "+", ".", "-.", "+."}:
            if self._numeric_range_is_int and "." in text:
                self.setText(self._last_valid_text)
            return

        try:
            value = int(text) if self._numeric_range_is_int else float(text)
        except ValueError:
            self.setText(self._last_valid_text)
            return

        if self.min_val <= value <= self.max_val:
            self._last_valid_text = text
            return

        self.setText(self._last_valid_text)

    def value(self):
        try:
            return float(self.text())
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
            self.apply_style(error=True)
            return

        if message == "":
            self.apply_style(error=False)
            return

        QToolTip.showText(self.mapToGlobal(self.rect().bottomLeft()), message)
        self.apply_style(error=True)