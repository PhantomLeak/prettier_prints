# ANSI coloring for terminal output messages
STYLING_OPTIONS = {
    "pref": "\033[",
    "reset": "\033[0m",
    # Colors
    "standard_colors": {
        "black": "30m",
        "red": "31m",
        "green": "32m",
        "yellow": "33m",
        "blue": "34m",
        "magenta": "35m",
        "cyan": "36m",
        "white": "37m"
    },
    # Bright Colors
    "bright_colors": {
        "bright_red": "31;1m",
        "bright_green": "32;1m",
        "bright_yellow": "33;1m",
        "bright_blue": "34;1m",
        "bright_magenta": "35;1m",
        "bright_cyan": "36;1m",
        "bright_white": "37;1m",
    },
    # Styling
    "bold": "\033[1m",
    "underline": "\033[4m",
    "highlight": "\033[7m",
}