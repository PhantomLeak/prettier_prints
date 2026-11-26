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


T = TypeVar('T', bound='_Styleable')


class _Styleable:
    def __init__(self, message: str = ''):
        self.output_message = message

    def _wrap(self: T, open_code: str, close_code: str) -> T:
        # Build a NEW instance of whatever class we are (e.g. Output); never mutate self
        return type(self)(f"{open_code}{self.output_message}{close_code}")


class Decorators(_Styleable):
    def bold(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['bold'], _reset())

    def underline(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['underline'], _reset())

    def highlight(self: T) -> T:
        return self._wrap(STYLING_OPTIONS['highlight'], _reset())


class Colors(_Styleable):
    def red(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['red']}", _reset())

    def green(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['green']}", _reset())

    def yellow(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['yellow']}", _reset())

    def blue(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['blue']}", _reset())

    def magenta(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['magenta']}", _reset())

    def cyan(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['cyan']}", _reset())

    def white(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['standard_colors']['white']}", _reset())

    def bright_red(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_red']}", _reset())

    def bright_green(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_green']}", _reset())

    def bright_yellow(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_yellow']}", _reset())

    def bright_blue(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_blue']}", _reset())

    def bright_magenta(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_magenta']}", _reset())

    def bright_cyan(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_cyan']}", _reset())

    def bright_white(self: T) -> T:
        return self._wrap(f"{_pref()}{STYLING_OPTIONS['bright_colors']['bright_white']}", _reset())
