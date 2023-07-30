# ANSI coloring for terminal output messages
class PrettierPrints:
    pref = "\033["
    bold_pref = "\033[1m"
    reset = f"{pref}0m"
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"

    def __init__(self):
        pass

    # Custom message with color options rather than a set color output
    def print(self, color: str = green, message: str = '', bold_text: bool = False):
        prefex_string = ''
        if bold_text:
            prefex_string += f'{self.bold_pref}'
        prefex_string += f'{self.pref}{color}'

        print(f'{prefex_string}{message}{self.reset} ')

    def output_message(self, color_one: str = 'green', msg: str = '',
                       color_two: str = 'white', output: str = 'white'):
        print(f'{self.pref}{color_one}{msg} -> {self.reset} {self.pref}{color_two}{output}{self.reset}')


if __name__ == '__main__':
    test = PrettierPrints()
    test.print(message='cool', color=test.red)
