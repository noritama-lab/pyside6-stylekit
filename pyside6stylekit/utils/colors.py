# utils/colors.py
def normalize_color(color):
    css_colors = {
        "red": "#ff0000", "green": "#00ff00", "blue": "#0000ff",
        "black": "#000000", "white": "#ffffff", "gray": "#808080",
        "orange": "#ffa500", "yellow": "#ffff00", "purple": "#800080",
        "pink": "#ffc0cb", "sky": "#87ceeb",
    }

    if isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
        return f"#{r:02x}{g:02x}{b:02x}"

    if isinstance(color, str):
        if color.startswith("#") and len(color) == 7:
            return color.lower()
        if color.lower() in css_colors:
            return css_colors[color.lower()]

    raise ValueError(f"Invalid color: {color}")


def adjust_color(color, factor):
    color = color.lstrip("#")
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    r = max(0, min(255, int(r * factor)))
    g = max(0, min(255, int(g * factor)))
    b = max(0, min(255, int(b * factor)))

    return f"#{r:02x}{g:02x}{b:02x}"