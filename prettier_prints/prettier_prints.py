# ANSI coloring for terminal output messages
import json as _json  # aliased: PrettierPrints has a method named json
from typing import Optional

from prettier_prints.ansi_styling import STYLING_OPTIONS


class PrettierPrints:
    def __init__(self, style: Optional[str] = None):
        self.style = style

    # Custom message with color options rather than a set color output
    def out(self, msg: Optional[str] = None, style: Optional[str] = None,
            json_out: Optional[dict] = None):
        json_out = json_out or {}  # None default: a {} default would be shared across calls

        if msg is None:
            msg = json_out.get('msg')

        # Only a missing message is an error; 0, False and '' are valid messages
        if msg is None:
            raise ValueError("A message is required")

        if style is None:
            style = json_out.get('style')

        if style is None:
            style = self.style

        style_codes = self.get_styling_info(styling=style, formatted_string='') if style is not None else ''

        # No recognised styling: return the plain message, never a dangling escape prefix
        if not style_codes:
            return f"{msg}"

        return f"{style_codes}{msg}{STYLING_OPTIONS['reset']}"

    def json(self, json_obj, style: Optional[str] = None):
        # Prints the styled JSON (unchanged public behavior); see json_str() for the string
        print(self.json_str(json_obj, style))

    def json_str(self, json_obj, style: Optional[str] = None) -> str:
        # Returns styled JSON of any depth. With ANSI codes stripped, the output is
        # identical to json.dumps(json_obj, indent=2, ensure_ascii=False).
        # Empty {} / [] are valid JSON; only a missing object is an error.
        if json_obj is None:
            raise ValueError("Must be a valid JSON object")

        codes = {kind: self.get_styling_info(styling=s)
                 for kind, s in self.strip_styling_for_json(style).items()}
        return self._format_json(json_obj, codes, level=0)

    def _format_json(self, value, codes, level) -> str:
        pad, inner = '  ' * level, '  ' * (level + 1)

        if isinstance(value, dict):
            if not value:
                return '{}'
            lines = []
            for key, val in value.items():
                # A key is colored by the type of its value: dict, list, or anything else (string)
                if isinstance(val, dict):
                    kind = 'dict'
                elif isinstance(val, (list, tuple)):
                    kind = 'list'
                else:
                    kind = 'string'
                key_text = self._paint(_json.dumps(self._json_key(key), ensure_ascii=False), codes[kind])
                lines.append(f"{inner}{key_text}: {self._format_json(val, codes, level + 1)}")
            return '{\n' + ',\n'.join(lines) + f'\n{pad}}}'

        if isinstance(value, (list, tuple)):
            if not value:
                return '[]'
            items = []
            for item in value:
                text = self._format_json(item, codes, level + 1)
                if not isinstance(item, (dict, list, tuple)):
                    text = self._paint(text, codes['string'])
                items.append(f"{inner}{text}")
            return '[\n' + ',\n'.join(items) + f'\n{pad}]'

        # Scalars (values stay uncolored): json handles quoting, escaping, true/false/null.
        # Non-JSON types (datetime, set, ...) fall back to a quoted str() instead of crashing.
        return _json.dumps(value, ensure_ascii=False, default=str)

    @staticmethod
    def _json_key(key) -> str:
        # Match json.dumps key conversion: True -> "true", None -> "null", 1 -> "1"
        if isinstance(key, str):
            return key
        if isinstance(key, (bool, int, float)) or key is None:
            return _json.dumps(key)
        return str(key)

    @staticmethod
    def _paint(text, code) -> str:
        return f"{code}{text}{STYLING_OPTIONS['reset']}" if code else text

    def strip_styling_for_json(self, styling):
        return_styling = {
            'list': 'red',
            'dict': 'magenta',
            'string': 'green'
        }
        aliases = {'str': 'string'}  # README documents str=

        if not styling:
            return return_styling

        # "list=blue;bold&dict=red&string=green" -> one "type=styles" setting per '&'
        for part in styling.split('&'):
            if '=' not in part:
                continue  # ignore malformed pieces
            key, value = part.split('=', 1)
            key = key.strip()
            key = aliases.get(key, key)
            if key in return_styling:
                return_styling[key] = value.strip()

        return return_styling

    def get_styling_info(self, styling, formatted_string=''):
        # Returns formatted_string + complete escape sequences for the requested styles.
        # Color is only emitted if one was named (no forced white default).
        color = ''
        formatted_style = ''
        specified_styles = styling.split(';')

        for styles in specified_styles:
            styles = styles.strip()
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