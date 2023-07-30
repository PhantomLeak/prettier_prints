# ANSI coloring for terminal output messages
class Colors:
    pref = "\033["
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
    def print(self, color: str = 'green', message: str = ''):
        return f'{self.pref}{color}{message}{self.reset} '

    def output_message(self, color_one: str = 'green', msg: str = '',
                       color_two: str = 'white', output: str = 'white'):
        return f'{self.pref}{color_one}{msg} -> {self.reset} {self.pref}{color_two}{output}{self.reset}'
