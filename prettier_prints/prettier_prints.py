# ANSI coloring for terminal output messages
STYLING_OPTIONS = {
    "pref": "\033[",
    "reset": "\033[0m",
    # Colors
    "black": "30m",
    "red": "31m",
    "green": "32m",
    "yellow": "33m",
    "blue": "34m",
    "magenta": "35m",
    "cyan": "36m",
    "white": "37m",
    # Bright Colors
    "bright_red": "31;1m",
    "bright_green": "32;1m",
    "bright_yellow": "33;1m",
    "bright_blue": "34;1m",
    "bright_magenta": "35;1m",
    "bright_cyan": "36;1m",
    "bright_white": "37;1m",
    # Styling
    "bold": "\033[1m",
    "underline": "\033[4m",
    "highlight": "\033[7m",
}
class PrettierPrints:
    def __init__(self, style: str = None):
        self.style = style

    # Custom message with color options rather than a set color output
    def out(self, msg: str = None, style: str = None, print_msg: dict = {}):
        if msg is None and print_msg != {}:
            msg = print_msg.get('msg')

        if not msg:
            raise Exception('Msg is a required key')

        formatted_msg = f"{STYLING_OPTIONS['pref']}"

        if style is None and print_msg != {}:
            style = print_msg.get('style')

        if style is not None:
            formatted_msg = self.get_styling_info(styling=style, formatted_string=formatted_msg)
        elif self.style is not None:
            formatted_msg = self.get_styling_info(styling=self.style, formatted_string=formatted_msg)

        formatted_msg += f"{msg}{STYLING_OPTIONS['reset']}"
        return formatted_msg

    def get_styling_info(self, styling, formatted_string):
        specified_styles = styling.split(';')
        for styles in specified_styles:
            style = STYLING_OPTIONS.get(styles.lower())
            if style:  # TODO: Check if not style and do a possible predefine if it was a color attempt
                formatted_string += style
        return formatted_string


if __name__ == '__main__':
    pp = PrettierPrints()
    pp.style = 'Blue;bold;underline'
    print(f'This is a test -> {pp.out(msg="And it works")}')
