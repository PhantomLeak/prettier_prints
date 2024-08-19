# ANSI coloring for terminal output messages
# Old v1 version of the prettier prints module
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


def _pref() -> str:
    return STYLING_OPTIONS['pref']


def _reset() -> str:
    return STYLING_OPTIONS['reset']


class Decorators:
    def __init__(self, message: str = ''):
        self.output_message = message

    def bold(self) -> 'Decorators':
        self.output_message = f"{STYLING_OPTIONS['bold']}{self.output_message}{_reset()}"
        return self

    def underline(self) -> 'Decorators':
        self.output_message = f"{STYLING_OPTIONS['underline']}{self.output_message}{_reset()}"
        return self

    def highlight(self) -> 'Decorators':
        self.output_message = f"{STYLING_OPTIONS['highlight']}{self.output_message}{_reset()}"
        return self


class Colors:
    def __init__(self, message: str = ''):
        self.output_message = message
    
    def red(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['red']}{self.output_message}{_reset()}"
        return self

    def green(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['green']}{self.output_message}{_reset()}"
        return self

    def yellow(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['yellow']}{self.output_message}{_reset()}"
        return self

    def blue(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['blue']}{self.output_message}{_reset()}"
        return self
    
    def magenta(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['magenta']}{self.output_message}{_reset()}"
        return self

    def cyan(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['cyan']}{self.output_message}{_reset()}"
        return self

    def white(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['standard_colors']['white']}{self.output_message}{_reset()}"
        return self

    def bright_red(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_red']}{self.output_message}{_reset()}"
        return self

    def bright_green(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_green']}{self.output_message}{_reset()}"
        return self

    def bright_yellow(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_yellow']}{self.output_message}{_reset()}"
        return self

    def bright_blue(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_blue']}{self.output_message}{_reset()}"
        return self

    def bright_magenta(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_magenta']}{self.output_message}{_reset()}"
        return self

    def bright_cyan(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_cyan']}{self.output_message}{_reset()}"
        return self

    def bright_white(self) -> 'Colors':
        self.output_message = f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_white']}{self.output_message}{_reset()}"
        return self