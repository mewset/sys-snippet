# sys-snippet

A minimal CLI tool that prints system info in your terminal or generates a ready-to-paste markdown block for your README.

## 🚀 Features

✅ OS, kernel, uptime, shell, WM/DE, RAM  
✅ Colored terminal output  
✅ `--markdown` for markdown block  
✅ `--copy` to copy markdown directly to clipboard (xclip/pbcopy)

## 🔧 Installation

```bash
git clone https://github.com/yourusername/sys-snippet.git
cd sys-snippet
pip install .
```

## ⚡ Usage

```bash
sys-snippet
sys-snippet --markdown
sys-snippet --markdown --copy
```

## 📌 Example

**Terminal output:**
```
System Info:
OS: Arch Linux
Kernel: 6.9.2
...
```

**Markdown output:**
```yaml
OS: Arch Linux
Kernel: 6.9.2
Uptime: 3 hours, 22 mins
Shell: /bin/zsh
WM/DE: Hyprland
RAM: 1.2G / 7.8G
```

## 🪪 License

MIT
