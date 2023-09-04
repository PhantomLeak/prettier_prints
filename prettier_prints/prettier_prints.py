# ANSI coloring for terminal output messages
from ansi_styling import STYLING_OPTIONS
import json


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

    def json(self, json_obj):
        if json_obj == {} or json_obj is None:
            raise Exception("Must be a valid JSON object")
        print('{')
        for key in json_obj.keys():
            if type(json_obj[key]) == dict:
                print(f"{STYLING_OPTIONS['pref']}{STYLING_OPTIONS['standard_colors']['blue']} {key} {STYLING_OPTIONS['reset']}: {str('{')}")
                for inner_key in json_obj[key].keys():
                    print(f"{' ' * 2}{STYLING_OPTIONS['pref']}{STYLING_OPTIONS['standard_colors']['red']} {inner_key} {STYLING_OPTIONS['reset']}: {json_obj[key][inner_key]}")
                print(' }')
            else:
                print(f"{STYLING_OPTIONS['pref']}{STYLING_OPTIONS['standard_colors']['blue']} {key} {STYLING_OPTIONS['reset']}: {json_obj[key]}")

        print('}')

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
    pp.style = 'bright_red;bold;underline'
    pp.json(json_obj={'test': 'cool', 'test_two': 'cool_two', 'dict_check': {'test': 'hello'}, 'list_check': []})
    # print(f'This is a test -> {pp.out(msg="And it works")}')
    # print(f'This is a test -> {pp.out(msg="And it works", style="bright_blue;underline")}')
    # print(f'This is a test -> {pp.out(msg="And it works", style="blue;underline")}')
    # print('\033[48;5;36m\033[38;5;41m TEXTHERE \033[0;0m')
