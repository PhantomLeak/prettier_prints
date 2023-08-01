# ANSI coloring for terminal output messages
class PrettierPrints:
    pref = "\033["
    reset = f"{pref}0m"
    # Colors
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"
    # Bright Colors
    bright_red = "31;1m"
    bright_green = "32;1m"
    bright_yellow = "33;1m"
    bright_blue = "34;1m"
    bright_magenta = "35;1m"
    bright_cyan = "36;1m"
    bright_white = "37;1m"
    # Styling
    bold = "\033[1m"
    underline = "\033[4m"
    reversed = "\033[7m"

    def __init__(self):
        pass

    # Custom message with color options rather than a set color output
    def print(self, color: str = green, message: str = ''):
        prefex_string = ''
        prefex_string += f'{self.pref}{color}'

        print(f'{prefex_string}{message}{self.reset} ')

    def output_message(self, color_one: str = 'green', msg: str = '',
                       color_two: str = 'white', output: str = 'white'):
        print(f'{self.pref}{color_one}{msg} -> {self.reset} {self.pref}{color_two}{output}{self.reset}')


if __name__ == '__main__':
    test = PrettierPrints()
    test.print(message='cool', color=test.red)
