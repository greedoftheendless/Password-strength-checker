# 🔐 Password Strength Checker & Custom Wordlist Generator (TUI)

This terminal-based application helps users evaluate password strength and generate custom wordlists for penetration testing, CTFs, and personal cybersecurity practice. Built with a TUI (Textual User Interface), it blends simplicity with functionality for offline, CLI-first environments.

---

## 📦 Features

- ✅ Real-time password strength analysis
- 🧠 Custom wordlist generation based on personal data patterns
- 🎯 Suggestions to improve weak passwords
- 💡 Emoji bar and messages for instant feedback
- ⌨️ Keyboard navigation via Textual library

---

## 🛠 Tools & Technologies

- **Python 3.10+**
- [`textual`](https://github.com/Textualize/textual) — for TUI
- `re` (regex) — for pattern evaluation
- `argparse` / `sys` — for CLI parameters (if applicable)

---

## 📋 How It Works

1. Launch the TUI with:
   ```bash
   python tui_app.py
