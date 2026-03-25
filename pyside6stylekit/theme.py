# theme.py
from .presets import SIZE_PRESETS
from .utils.colors import normalize_color, adjust_color

class Theme:
    def __init__(self, primary="blue", mode="light",
                 font_family="Segoe UI", size="mid"):
        self.primary = normalize_color(primary)
        self.mode = mode
        self.font_family = font_family
        self.size = size

        if size not in SIZE_PRESETS:
            raise ValueError("size must be small / mid / large")

        if mode == "light":
            self.text_color = "#000000"
            self.background = "#ffffff"
            self.border_color = "#dcdde1"
        elif mode == "dark":
            self.text_color = "#ffffff"
            self.background = "#2f3640"
            self.border_color = "#4b4b4b"
        else:
            raise ValueError("mode must be light / dark")

    def hover(self):
        return adjust_color(self.primary, 0.85)

    def pressed(self):
        return adjust_color(self.primary, 0.70)

    def font_size(self):
        return SIZE_PRESETS[self.size]["font"]

    def padding(self):
        return SIZE_PRESETS[self.size]["padding"]

    def export_qss(self):
        return f"""
        * {{
            font-family: '{self.font_family}';
            color: {self.text_color};
            background: {self.background};
        }}
        """