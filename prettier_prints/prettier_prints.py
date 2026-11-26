# ANSI coloring for terminal output messages
from prettier_prints.ansi_styling import STYLING_OPTIONS
import re


class PrettierPrints:
    def __init__(self, style: str = None):
        self.style = style

    # Custom message with color options rather than a set color output
    def out(self, msg: str = None, style: str = None, json_out: dict = {}):
        if msg is None and json_out != {}:
            msg = json_out.get('msg')

        if not msg:
            raise Exception("A message is required")

        if style is None and json_out != {}:
            style = json_out.get('style')

        if style is None:
            style = self.style

        style_codes = self.get_styling_info(styling=style, formatted_string='') if style is not None else ''

        # No recognised styling: return the plain message, never a dangling escape prefix
        if not style_codes:
            return f"{msg}"

        return f"{style_codes}{msg}{STYLING_OPTIONS['reset']}"

    def json(self, json_obj, style: str = None):
        if json_obj == {} or json_obj is None:
            raise Exception("Must be a valid JSON object")

        json_style = self.strip_styling_for_json(style)

        print('{')
        for key in json_obj.keys():
            formatted_string = ''
            if type(json_obj[key]) == dict:
                dict_formatted_string = self.get_styling_info(styling=json_style['dict'], formatted_string=formatted_string)
                print(f"{dict_formatted_string}{key}{STYLING_OPTIONS['reset']}: {str('{')}")
                for inner_key in json_obj[key].keys():
                    print(f"{' ' * 2}{dict_formatted_string}{inner_key} {STYLING_OPTIONS['reset']}: {json_obj[key][inner_key]},")
                print(' },')

            elif type(json_obj[key]) == list:
                list_formatted_string = self.get_styling_info(styling=json_style['list'], formatted_string=formatted_string)
                print(f"{list_formatted_string}{key}{STYLING_OPTIONS['reset']}: {str('[')}")
                for item in json_obj[key]:
                    if type(item) == dict:
                        dict_formatted_string = self.get_styling_info(styling=json_style['dict'], formatted_string=formatted_string)
                        print(' ' * 3 + '{')
                        for inner_key in item.keys():
                            print(f"{' ' * 4}{dict_formatted_string}{inner_key} {STYLING_OPTIONS['reset']}: {item[inner_key]},")
                        print(' ' * 3 + '},')
                    else:
                        string_formatted_string = self.get_styling_info(styling=json_style['string'], formatted_string=formatted_string)
                        print(f"{' ' * 2}{string_formatted_string}{item}{STYLING_OPTIONS['reset']}")
                print(' ],')

            else:
                string_formatted_string = self.get_styling_info(styling=json_style['string'], formatted_string=formatted_string)
                print(f"{string_formatted_string}{key}{STYLING_OPTIONS['reset']}: {json_obj[key]},")

        print('}')

    def strip_styling_for_json(self, styling):
        return_styling = {
            'list': 'red',
            'dict': 'magenta',
            'string': 'green'
        }
        if styling is not None:
            if re.search('string=(.*?)', styling):
                if re.search('string=(.*?)&', styling):
                    return_styling['string'] = re.search('string=(.*?)&', styling).group(1)
                elif re.search('&string=(.*?)', styling):
                    return_styling['string'] = re.search('&string=(.*?)$', styling).group(1)

            if re.search('list=(.*?)', styling):
                if re.search('list=(.*?)&', styling):
                    return_styling['list'] = re.search('list=(.*?)&', styling).group(1)
                elif re.search('&list=(.*?)', styling):
                    return_styling['list'] = re.search('&list=(.*?)$', styling).group(1)

            if re.search('dict=(.*?)', styling):
                if re.search('dict=(.*?)&', styling):
                    return_styling['dict'] = re.search('dict=(.*?)&', styling).group(1)
                elif re.search('&dict=(.*?)', styling):
                    return_styling['dict'] = re.search('&dict=(.*?)$', styling).group(1)

        return return_styling

    def get_styling_info(self, styling, formatted_string=''):
        # Returns formatted_string + complete escape sequences for the requested styles.
        # Color is only emitted if one was named (no forced white default).
        color = ''
        formatted_style = ''
        specified_styles = styling.split(';')

        for styles in specified_styles:
            if STYLING_OPTIONS["standard_colors"].get(styles):
                color = f'{STYLING_OPTIONS["pref"]}{STYLING_OPTIONS["standard_colors"][styles]}'
            elif STYLING_OPTIONS["bright_colors"].get(styles):
                color = f'{STYLING_OPTIONS["pref"]}{STYLING_OPTIONS["bright_colors"][styles]}'
            elif styles in ('bold', 'underline', 'highlight'):
                formatted_style += STYLING_OPTIONS[styles]

        formatted_string += f'{color}{formatted_style}'
        return formatted_string


if __name__ == '__main__':
    pp = PrettierPrints()
    pp.json(json_obj={'test': 'cool', 'test_two': 'cool_two', 'dict_check': {'test': 'hello'},
                      'list_check': [
                          'test',
                          'test two',
                          {
                              'test': 'hello',
                              'test_two': 'bloop'
                          },
                          {
                              'test': 'hello',
                              'test_two': 'bloop'
                          }
                      ]}, style='list=blue;underline&dict=red;bold&string=green;')

    # print(pp.strip_styling_for_json('string=red;underline&list=blue&dict=green;underline'))