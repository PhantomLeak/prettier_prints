import contextlib
import io
import json
import re
import unittest
from prettier_prints.prettier_prints import PrettierPrints
from tests.helpers import VisualTestCase

RESET = "\033[0m"


class TestOut(VisualTestCase):
    def setUp(self):
        self.pp = PrettierPrints()

    # Bug 6: no style must not emit a dangling "\033[" prefix
    def test_no_style_returns_plain_message(self):
        self.assertEqual(self.pp.out(msg='Hi'), 'Hi')
        self.assertNotIn("\033", self.pp.out(msg='Hi'))

    def test_unknown_style_returns_plain_message(self):
        self.assertEqual(self.pp.out(msg='Hi', style='not_a_style'), 'Hi')

    def test_internal_keys_are_not_styles(self):
        # 'pref'/'reset' are STYLING_OPTIONS keys, not user styles
        self.assertEqual(self.pp.out(msg='Hi', style='pref;reset'), 'Hi')

    # Bug 7: modifier-only styles keep the terminal's color and are well-formed
    def test_modifier_only_does_not_force_white(self):
        result = self.pp.out(msg='Hi', style='bold')
        self.assertEqual(result, f"\033[1mHi{RESET}")
        self.assertNotIn("37m", result)

    def test_color_and_modifiers(self):
        self.assertEqual(self.pp.out(msg='Hi', style='red;bold'), f"\033[31m\033[1mHi{RESET}")
        self.assertEqual(self.pp.out(msg='Hi', style='blue;bold;underline'),
                         f"\033[34m\033[1m\033[4mHi{RESET}")

    def test_bright_color(self):
        self.assertEqual(self.pp.out(msg='Hi', style='bright_red'), f"\033[91mHi{RESET}")

    def test_instance_default_style_and_override(self):
        pp = PrettierPrints(style='green')
        self.assertEqual(pp.out(msg='Hi'), f"\033[32mHi{RESET}")
        self.assertEqual(pp.out(msg='Hi', style='blue'), f"\033[34mHi{RESET}")

    def test_json_out_param(self):
        self.assertEqual(self.pp.out(json_out={'msg': 'Hi', 'style': 'yellow'}), f"\033[33mHi{RESET}")
        self.assertEqual(self.pp.out(json_out={'msg': 'Hi'}), 'Hi')

    def test_every_escape_sequence_is_well_formed(self):
        # Each "\033[" must be followed by digits/semicolons and an 'm'
        import re
        for style in ['bold', 'underline', 'highlight', 'red;bold', 'bright_cyan;underline;highlight']:
            with self.subTest(style=style):
                result = self.pp.out(msg='Hi', style=style)
                self.assertEqual(len(re.findall(r"\033\[", result)),
                                 len(re.findall(r"\033\[[0-9;]+m", result)))

    def test_visual_swatch(self):
        # Run `pytest -s` (default via pytest.ini) to see these in the terminal
        self.show()
        for style in ['', 'bold', 'underline', 'highlight', 'red;bold', 'bright_blue;underline']:
            self.show(f"  {style or '(no style)':<24}{self.pp.out(msg='Sample text', style=style or None)}")


class TestJsonStyleParsing(VisualTestCase):
    def setUp(self):
        self.pp = PrettierPrints()
        self.defaults = {'list': 'red', 'dict': 'magenta', 'string': 'green'}

    # Bug 8: a lone setting (no '&' around it) used to be silently dropped
    def test_single_setting_is_applied(self):
        self.assertEqual(self.pp.strip_styling_for_json('string=red')['string'], 'red')
        self.assertEqual(self.pp.strip_styling_for_json('list=blue')['list'], 'blue')
        self.assertEqual(self.pp.strip_styling_for_json('dict=cyan')['dict'], 'cyan')

    def test_single_setting_keeps_other_defaults(self):
        result = self.pp.strip_styling_for_json('string=red')
        self.assertEqual((result['list'], result['dict']), ('red', 'magenta'))

    def test_multiple_settings_any_order(self):
        result = self.pp.strip_styling_for_json('dict=red;bold&string=cyan&list=blue')
        self.assertEqual(result, {'list': 'blue', 'dict': 'red;bold', 'string': 'cyan'})

    def test_str_alias(self):
        self.assertEqual(self.pp.strip_styling_for_json('str=yellow')['string'], 'yellow')

    def test_whitespace_tolerated(self):
        result = self.pp.strip_styling_for_json(' list = blue & dict=red ')
        self.assertEqual((result['list'], result['dict']), ('blue', 'red'))
        self.assertEqual(self.pp.out(msg='Hi', style='red; bold'), "\033[31m\033[1mHi\033[0m")

    def test_none_empty_and_unknown_keep_defaults(self):
        for style in (None, '', 'foo=red', 'garbage'):
            with self.subTest(style=style):
                self.assertEqual(self.pp.strip_styling_for_json(style), self.defaults)

    def test_visual_json_single_setting(self):
        # Run `pytest --output` to see strings in cyan here
        self.show("\n  json() with style='string=cyan':")
        self.show(self.pp.json_str({'name': 'demo', 'tags': ['a', 'b'], 'meta': {'k': 'v'}}, style='string=cyan'))


ANSI = re.compile(r"\033\[[0-9;]*m")

DEEP_OBJ = {
    'name': 'demo',
    'active': True,
    'score': 9.5,
    'missing': None,
    'unicode': 'café ☕',
    'meta': {
        'level2': {
            'level3': {'level4': 'deep'},
            'count': 3,
        },
        'empty_dict': {},
        'empty_list': [],
    },
    'items': [
        'plain',
        42,
        {'id': 1, 'tags': ['x', 'y']},
        [1, [2, 3]],
    ],
}


def strip_ansi(text):
    return ANSI.sub('', text)


class TestJsonStr(VisualTestCase):
    def setUp(self):
        self.pp = PrettierPrints()
        # distinct colors per type so assertions can tell them apart
        self.style = 'dict=magenta&list=blue&string=green'
        self.dict_c, self.list_c, self.str_c = "\033[35m", "\033[34m", "\033[32m"

    # Bug 9: any depth, and the uncolored text is exactly json.dumps output
    def test_matches_json_dumps_when_uncolored(self):
        result = strip_ansi(self.pp.json_str(DEEP_OBJ, style=self.style))
        self.assertEqual(result, json.dumps(DEEP_OBJ, indent=2, ensure_ascii=False))
        self.assertEqual(json.loads(result), DEEP_OBJ)

    def test_keys_colored_by_value_type_at_every_depth(self):
        result = self.pp.json_str(DEEP_OBJ, style=self.style)
        self.assertIn(f'{self.dict_c}"meta"{RESET}', result)        # depth 1, dict value
        self.assertIn(f'{self.list_c}"items"{RESET}', result)       # depth 1, list value
        self.assertIn(f'{self.str_c}"name"{RESET}', result)         # depth 1, scalar value
        self.assertIn(f'{self.dict_c}"level2"{RESET}', result)      # depth 2, dict value
        self.assertIn(f'{self.list_c}"empty_list"{RESET}', result)  # depth 2, list value
        self.assertIn(f'{self.str_c}"count"{RESET}', result)        # depth 3, scalar value
        self.assertIn(f'{self.str_c}"level4"{RESET}', result)       # depth 4, scalar value

    def test_list_scalars_use_string_style_and_values_stay_uncolored(self):
        result = self.pp.json_str(DEEP_OBJ, style=self.style)
        self.assertIn(f'{self.str_c}"plain"{RESET}', result)        # scalar in list
        self.assertIn(f'{self.str_c}42{RESET}', result)
        self.assertIn(f': "demo"', result)                          # dict value: uncolored
        self.assertIn(': true', result)
        self.assertIn(': null', result)

    def test_top_level_list(self):
        obj = [{'a': 1}, 'b']
        result = self.pp.json_str(obj)
        self.assertEqual(strip_ansi(result), json.dumps(obj, indent=2))

    def test_no_color_style_emits_no_codes(self):
        result = self.pp.json_str({'a': {'b': [1]}}, style='dict=&list=&string=')
        self.assertNotIn("\033", result)

    def test_tuple_and_non_json_types(self):
        import datetime
        obj = {'pair': (1, 2), 'when': datetime.date(2026, 1, 2), 1: 'int key', None: 'none key'}
        result = strip_ansi(self.pp.json_str(obj))
        self.assertEqual(json.loads(result),
                         {'pair': [1, 2], 'when': '2026-01-02', '1': 'int key', 'null': 'none key'})

    def test_json_str_none_raises_but_empty_is_valid(self):
        with self.assertRaises(ValueError):
            self.pp.json_str(None)
        self.assertEqual(self.pp.json_str({}), '{}')
        self.assertEqual(self.pp.json_str([]), '[]')

    def test_json_prints_same_as_json_str(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            returned = self.pp.json(DEEP_OBJ, style=self.style)
        self.assertIsNone(returned)
        self.assertEqual(buffer.getvalue(), self.pp.json_str(DEEP_OBJ, style=self.style) + '\n')

    def test_visual_deep_json(self):
        self.show("\n  json() deep object, style='dict=magenta&list=blue&string=green':")
        self.show(self.pp.json_str(DEEP_OBJ, style=self.style))


class TestInputValidation(unittest.TestCase):
    def setUp(self):
        self.pp = PrettierPrints()

    # Bug 10b: falsy-but-present messages are valid
    def test_falsy_messages_are_valid(self):
        self.assertEqual(self.pp.out(msg=0), '0')
        self.assertEqual(self.pp.out(msg=False), 'False')
        self.assertEqual(self.pp.out(msg=0, style='red'), "\033[31m0\033[0m")
        self.assertEqual(self.pp.out(msg=''), '')
        self.assertEqual(self.pp.out(json_out={'msg': 0}), '0')

    # Bug 10c: missing message raises ValueError (still an Exception subclass)
    def test_missing_message_raises_value_error(self):
        for kwargs in ({}, {'json_out': {}}, {'json_out': {'style': 'red'}}, {'json_out': None}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    self.pp.out(**kwargs)

    # Bug 10a: no shared mutable default
    def test_json_out_default_is_not_shared(self):
        import inspect
        self.assertIsNone(inspect.signature(PrettierPrints.out).parameters['json_out'].default)

    def test_msg_param_takes_precedence_over_json_out(self):
        self.assertEqual(self.pp.out(msg='a', json_out={'msg': 'b', 'style': 'red'}), f"\033[31ma{RESET}")


if __name__ == '__main__':
    unittest.main()
