#!/usr/bin/env python3

import os
import platform
import subprocess
import argparse
import shutil

def get_os():
    """Get the pretty OS name from /etc/os-release or fallback to platform."""
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    return line.split("=")[1].strip().strip('"')
    except:
        return platform.system()

def get_kernel():
    """Get the kernel version."""
    return platform.release()

def get_uptime():
    """Get system uptime using 'uptime -p'."""
    try:
        output = subprocess.check_output(["uptime", "-p"]).decode().strip()
        return output
    except:
        return "N/A"

def get_shell():
    """Get the current shell from the environment."""
    return os.environ.get("SHELL", "Unknown")

def get_wm():
    """Get the current Window Manager or Desktop Environment."""
    return os.environ.get("XDG_CURRENT_DESKTOP", "Unknown")

def get_ram():
    """Get RAM usage using 'free -h'."""
    try:
        output = subprocess.check_output(["free", "-h"]).decode().splitlines()
        mem_line = [line for line in output if "Mem:" in line][0]
        used = mem_line.split()[2]
        total = mem_line.split()[1]
        return f"{used} / {total}"
    except:
        return "N/A"

def print_terminal(info):
    """Print system info to terminal with colors."""
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print(f"{BOLD}System Info:{RESET}")
    for key, value in info.items():
        print(f"{BLUE}{key}:{RESET} {GREEN}{value}{RESET}")

def format_markdown(info):
    """Format system info as a markdown code block."""
    lines = [f"{key}: {value}" for key, value in info.items()]
    md = "```yaml\n" + "\n".join(lines) + "\n```"
    return md

def copy_to_clipboard(text):
    """Copy text to clipboard using xclip (Linux) or pbcopy (macOS)."""
    if shutil.which("xclip"):
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode())
    elif shutil.which("pbcopy"):
        subprocess.run(["pbcopy"], input=text.encode())
    else:
        print("Clipboard tool not found (xclip or pbcopy). Skipping copy.")

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Print system info in terminal or as markdown.")
    parser.add_argument("--markdown", action="store_true", help="Output as markdown block")
    parser.add_argument("--copy", action="store_true", help="Copy markdown block to clipboard")

    args = parser.parse_args()

    info = {
        "OS": get_os(),
        "Kernel": get_kernel(),
        "Uptime": get_uptime(),
        "Shell": get_shell(),
        "WM/DE": get_wm(),
        "RAM": get_ram(),
    }

    if args.markdown:
        md = format_markdown(info)
        print(md)
        if args.copy:
            copy_to_clipboard(md)
    else:
        print_terminal(info)

if __name__ == "__main__":
    main()
