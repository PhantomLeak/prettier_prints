# ANSI coloring for terminal output messages
# Old v1 version of the prettier prints module
from typing import TypeVar

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
    # Bright Colors (true bright codes 91-97, not bold + color)
    "bright_colors": {
        "bright_black": "90m",
        "bright_red": "91m",
        "bright_green": "92m",
        "bright_yellow": "93m",
        "bright_blue": "94m",
        "bright_magenta": "95m",
        "bright_cyan": "96m",
        "bright_white": "97m",
    },
    # Styling
    "bold": "\033[1m",
    "underline": "\033[4m",
    "highlight": "\033[7m",
    # Codes that turn off a single style without resetting everything else
    "close": {
        "color": "\033[39m",
        "bold": "\033[22m",
        "underline": "\033[24m",
        "highlight": "\033[27m",
    },
}


def _pref() -> str:
    return STYLING_OPTIONS['pref']


def _reset() -> str:
    return STYLING_OPTIONS['reset']


T = TypeVar('T', bound='_Styleable')


class _Styleable:
    def __init__(self, message: str = ''):
        self.output_message = message

    def _wrap(self: T, open_code: str, close_code: str) -> T:
        # Re-apply our style wherever an inner style of the same type closed it,
        # then build a NEW instance of whatever class we are (e.g. Output); never mutate self
        inner = self.output_message.replace(close_code, close_code + open_code)
        return type(self)(f"{open_code}{inner}{close_code}")


class Decorators(_Styleable):
    def bold(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['bold'], STYLING_OPTIONS['close']['bold'])

    def underline(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['underline'], STYLING_OPTIONS['close']['underline'])

    def highlight(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['highlight'], STYLING_OPTIONS['close']['highlight'])


class Colors(_Styleable):
    def _color(self: T, code: str) -> T:
        return self._wrap(f"{_pref()}{code}", STYLING_OPTIONS['close']['color'])

    def black(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['black'])

    def red(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['red'])

    def green(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['green'])

    def yellow(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['yellow'])

    def blue(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['blue'])

    def magenta(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['magenta'])

    def cyan(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['cyan'])

    def white(self: T) -> T:
        return self._color(STYLING_OPTIONS['standard_colors']['white'])

    def bright_black(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_black'])

    def bright_red(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_red'])

    def bright_green(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_green'])

    def bright_yellow(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_yellow'])

    def bright_blue(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_blue'])

    def bright_magenta(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_magenta'])

    def bright_cyan(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_cyan'])

    def bright_white(self: T) -> T:
        return self._color(STYLING_OPTIONS['bright_colors']['bright_white'])
