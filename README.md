# PySide6StyleKit  
PySide6 アプリのための軽量で拡張性の高いスタイル済み UI コンポーネントキット。  
A lightweight and extensible styled UI component kit for PySide6 applications.

---

## 特徴 / Features
- 統一テーマ（ライト／ダーク／背景色）  
  Unified themes (light, dark, background-aware)
- スタイル済みウィジェット（Label / LineEdit / Button / Indus Alternate Button / Indus Lamp / Indus Momentary Button / CheckBox / RadioButton / ComboBox / Slider / ProgressBar / TextEdit / GroupBox など）  
  Styled widgets such as Label, LineEdit, Button, Indus Alternate Button, Indus Lamp, Indus Momentary Button, CheckBox, RadioButton, ComboBox, Slider, ProgressBar, TextEdit, and GroupBox
- GroupBox タイトルの自動中央揃え（フォントサイズ変更に追随）  
- 数値バリデーション（int / float / range）  
  Robust numeric validation (int, float, range)
- エラー表示の柔軟な制御（枠線のみ・メッセージ表示）  
  Flexible error signaling (border-only or message)
- 拡張しやすいモジュール構造  
  Modular and extensible architecture
- 実用的なサンプルコード付き  
  Includes practical example scripts

## v0.2.1 更新内容 / What's New
- `StyledLineEdit` を `QLineEdit` ベースに整理（内部合成から継承へ）
- `numeric_range` 入力の範囲制御を強化（範囲外入力を抑制）
- エラーメッセージは `show_error("...")` 呼び出し時にツールチップ表示
- `examples/demo.py` に Validate ボタンを表示

---

## インストール / Installation
```bash
pip install pyside6stylekit
```

---

## 使い方 / Usage
`examples/demo.py` と `examples/demo_indus.py` に基本的な使い方があります。  
Basic usage is available in `examples/demo.py` and `examples/demo_indus.py`.

### サポート widget / Supported widgets
- `StyledLabel`
- `StyledLineEdit`
- `StyledButton`
- `StyledCheckBox`
- `StyledRadioButton`
- `StyledComboBox`
- `StyledSlider`
- `StyledProgressBar`
- `StyledTextEdit`
- `StyledGroupBox`
- `IndusAlternateButton`, `IndusLamp`, `IndusMomentaryButton`

※ さらに `Theme` 本体で色やサイズ設定を管理し、各 widget のスタイルを統一しています。
### 利用可能なカラーモード / Available color modes
- `Theme.light()`
- `Theme.dark()`
- `Theme(primary=<hex>, mode='light'|'dark', background='<hex>')`

### サポート色（`utils/colors.py`） / Supported colors
`normalize_color` で次のキーワードを16進色に変換します:
- red: `#ff0000`
- green: `#00ff00`
- blue: `#0000ff`
- black: `#000000`
- white: `#ffffff`
- gray: `#808080`
- orange: `#ffa500`
- yellow: `#ffff00`
- purple: `#800080`
- pink: `#ffc0cb`
- sky: `#87ceeb`

`normalize_color` は `'#rrggbb'` 形式や `(r,g,b)` 形式も受け付けます。

### 色サンプル / Color samples
```python
from pyside6stylekit.utils.colors import normalize_color, adjust_color

print(normalize_color('sky'))       # #87ceeb
print(normalize_color((255,16,128)))  # #ff1080
print(adjust_color('#ff1080', 0.8))   # #cc0d66
```

```python
from pyside6stylekit import Theme, StyledLabel, StyledLineEdit, StyledButton, StyledGroupBox

theme = Theme.light()

label = StyledLabel("Hello")
lineedit = StyledLineEdit("Range (0-120)", theme, mode="numeric_range", min_val=0, max_val=120)
button = StyledButton("Submit")

# GroupBox with adaptive title positioning
groupbox = StyledGroupBox("Settings", theme)

# Validation examples
lineedit.show_error("Value out of range")  # tooltip + red border
lineedit.show_error("")                    # clear error state

```

---

## プロジェクト構造 / Project Structure
```
pyside6stylekit/
├─ pyside6stylekit/
│   ├─ utils/
│   │  ├─ __init__.py
│   │  └─ colors.py
│   ├─ widgets/
│   │  ├─ __init__.py
│   │  ├─ button.py
│   │  ├─ checkbox.py
│   │  ├─ combobox.py
│   │  ├─ groupbox.py
│   │  ├─ indus_alternate_button.py
│   │  ├─ indus_lamp.py
│   │  ├─ indus_momentary_button.py
│   │  ├─ label.py
│   │  ├─ lineedit.py
│   │  ├─ progressbar.py
│   │  ├─ radiobutton.py
│   │  ├─ slider.py
│   │  └─ textedit.py
│   ├─ __init__.py
│   ├─ presets.py
│   └─ theme.py
├─ examples/
│   ├─ demo.py
│   └─ demo_indus.py
├─ LICENSE
└─ README.md
```

---

## ライセンス / License
MIT License © 2026 Mitsunori

---

## 作者 / Author
Noritama-Lab
