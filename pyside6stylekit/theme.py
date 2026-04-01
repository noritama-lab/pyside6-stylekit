# theme.py
from .presets import SIZE_PRESETS
from .utils.colors import normalize_color, adjust_color


class Theme:
    def __init__(self, primary="blue", mode="light",
                 font_family="Segoe UI", size="mid",
                 text_color=None, background=None):
        self.primary = normalize_color(primary)
        self.mode = mode
        self.font_family = font_family
        self.size = size

        if size not in SIZE_PRESETS:
            raise ValueError("size must be small / mid / large")

        # -------------------------
        # 文字色（ユーザー指定 > モードデフォルト）
        # -------------------------
        if text_color:
            self.text_color = normalize_color(text_color)
        else:
            if mode == "light":
                self.text_color = "#000000"
            elif mode == "dark":
                self.text_color = "#ffffff"
            else:
                raise ValueError("mode must be light / dark")

        # 背景・枠色
        if background is not None:
            self.background = background
        else:
            if mode == "light":
                self.background = "#ffffff"
                self.border_color = "#dcdde1"
            else:
                self.background = "#2f3640"
                self.border_color = "#4b4b4b"
            return

        # backgroundが指定されてる場合、枠色もmode依存で設定
        if mode == "light":
            self.border_color = "#dcdde1"
        else:
            self.border_color = "#4b4b4b"

    # -------------------------
    # 色のバリエーション
    # -------------------------
    def primary_dark(self, factor=0.5):
        """OFF の時に使う暗い色"""
        return adjust_color(self.primary, factor)

    def hover(self):
        return adjust_color(self.primary, 0.85)

    def pressed(self):
        return adjust_color(self.primary, 0.70)

    # -------------------------
    # サイズ
    # -------------------------
    def font_size(self):
        return SIZE_PRESETS[self.size]["font"]

    def padding(self):
        return SIZE_PRESETS[self.size]["padding"]

    # -------------------------
    # QSS 出力
    # -------------------------
    def export_qss(self):
        return f"""
        * {{
            font-family: '{self.font_family}';
            color: {self.text_color};
            background: {self.background};
        }}
        """