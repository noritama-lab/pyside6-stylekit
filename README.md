# PySide6StyleKit  
PySide6 アプリのための軽量で拡張性の高いスタイル済み UI コンポーネントキット。  
A lightweight and extensible styled UI component kit for PySide6 applications.

---

## 特徴 / Features
- 統一テーマ（ライト／ダーク／背景色）  
  Unified themes (light, dark, background-aware)
- スタイル済みウィジェット（Label / LineEdit / Button など）  
  Styled widgets such as Label, LineEdit, and Button
- 数値バリデーション（int / float / range）  
  Robust numeric validation (int, float, range)
- エラー表示の柔軟な制御（枠線のみ・メッセージ表示）  
  Flexible error signaling (border-only or message)
- 拡張しやすいモジュール構造  
  Modular and extensible architecture
- 実用的なサンプルコード付き  
  Includes practical example scripts

---

## インストール / Installation
開発モードで利用する場合：  
For development mode:

```bash
pip install -e .
```

---

## 使い方 / Usage
`examples/demo.py` に基本的な使い方があります。  
Basic usage is available in `examples/demo.py`.

```python
from pyside6stylekit import Theme, StyledLabel, StyledLineEdit, StyledButton

theme = Theme.light()

label = StyledLabel("Hello")
lineedit = StyledLineEdit(validator="int")
button = StyledButton("Submit")
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
│   │  ├─ label.py
│   │  └─ lineedit.py
│   ├─ __init__.py
│   ├─ presets.py
│   └─ theme.py
├─ examples/
│   └─ demo.py
├─ LICENSE
├─ README.md
└─ pyproject.toml
```

---

## ライセンス / License
MIT License © 2026 Mitsunori

---

## 作者 / Author
Noritama-Lab
