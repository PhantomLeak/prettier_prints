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
class PrettierPrints:
    def __init__(self, style: str = None):
        self.style = style

    # Custom message with color options rather than a set color output
    def out(self, msg: str = None, style: str = None, json_out: dict = {}):
        if msg is None and json_out != {}:
            msg = json_out.get('msg')

        if not msg:
            raise Exception("A message is required")

        formatted_msg = f"{STYLING_OPTIONS['pref']}"

        if style is None and json_out != {}:
            style = json_out.get('style')

        if style is not None:
            formatted_msg = self.get_styling_info(styling=style, formatted_string=formatted_msg)
        elif self.style is not None:
            formatted_msg = self.get_styling_info(styling=self.style, formatted_string=formatted_msg)

        formatted_msg += f"{msg}{STYLING_OPTIONS['reset']}"
        return formatted_msg

    def get_styling_info(self, styling, formatted_string):
        color = STYLING_OPTIONS["standard_colors"]["white"]
        formatted_style = ''
        specified_styles = styling.split(';')

        for styles in specified_styles:
            if STYLING_OPTIONS["standard_colors"].get(styles):
                color = STYLING_OPTIONS["standard_colors"].get(styles)
            elif STYLING_OPTIONS["bright_colors"].get(styles):
                color = STYLING_OPTIONS["bright_colors"].get(styles)
            else:
                if STYLING_OPTIONS.get(styles):
                    formatted_style += STYLING_OPTIONS.get(styles)

        formatted_string += f'{color}{formatted_style}'

        return formatted_string


if __name__ == '__main__':
    pp = PrettierPrints()
    pp.style = 'bold;yellow;underline'
    print(f'This is a test -> {pp.out(msg="And it works")}')
