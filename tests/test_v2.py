import unittest
from prettier_prints.prettier_printsv2 import Output

# v2 color method name -> ANSI code. Bright variant is code + 60 (91-97).
# black is omitted until v2 gains black() (bug 4).
STANDARD_COLORS = {
    'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
    'magenta': 35, 'cyan': 36, 'white': 37,
}


class TestOutputImmutability(unittest.TestCase):
    def setUp(self):
        self.pp = Output()

    def test_results_do_not_alias(self):
        a = self.pp.msg('one').red()
        b = self.pp.msg('two').green().bold()

        self.assertIn('one', str(a))
        self.assertNotIn('two', str(a))
        self.assertIn('two', str(b))
        self.assertIsNot(a, b)

    def test_base_instance_never_mutated(self):
        self.pp.msg('one').red().bold()
        self.assertEqual(str(self.pp), '')

    def test_intermediate_results_preserved(self):
        plain = self.pp.msg('x')
        red = plain.red()
        self.assertEqual(str(plain), 'x')
        self.assertNotEqual(str(red), 'x')

    def test_chain_returns_output(self):
        result = self.pp.msg('x').red().bold().underline()
        self.assertIsInstance(result, Output)
        self.assertEqual(result.out(), str(result))

    def test_escape_output_closes_only_its_own_style(self):
        self.assertEqual(str(self.pp.msg('Hi').red()), "\033[31mHi\033[39m")
        self.assertEqual(str(self.pp.msg('Hi').yellow().bold()), "\033[1m\033[33mHi\033[39m\033[22m")
        self.assertEqual(str(self.pp.msg('Hi').underline()), "\033[4mHi\033[24m")
        self.assertEqual(str(self.pp.msg('Hi').highlight()), "\033[7mHi\033[27m")

    def test_all_standard_and_bright_colors(self):
        # Prints a side-by-side swatch; run `pytest -s` to see it in your terminal.
        print("\n  standard           bright")
        for name, code in STANDARD_COLORS.items():
            with self.subTest(color=name):
                standard = getattr(self.pp.msg(name.ljust(16)), name)()
                bright = getattr(self.pp.msg(f'bright_{name}'), f'bright_{name}')()
                print(f"  {standard}   {bright}")

                self.assertEqual(str(standard), f"\033[{code}m{name.ljust(16)}\033[39m")
                self.assertEqual(str(bright), f"\033[{code + 60}mbright_{name}\033[39m")
                # bright must be its own code, not bold + color
                self.assertNotIn("\033[1m", str(bright))

    def test_nested_different_styles(self):
        inner = self.pp.msg('file').bold()
        outer = self.pp.msg(f"Missing {inner} here").red()
        print(f"\n  nested bold in red:  {outer}")
        self.assertEqual(str(outer), "\033[31mMissing \033[1mfile\033[22m here\033[39m")
        self.assertNotIn("\033[0m", str(outer))

    def test_nested_same_style_type_restores_outer(self):
        inner = self.pp.msg('b').blue()
        outer = self.pp.msg(f"a {inner} c").red()
        print(f"\n  nested blue in red:  {outer}")
        # after blue closes, red is re-opened so " c" stays red
        self.assertEqual(str(outer), "\033[31ma \033[34mb\033[39m\033[31m c\033[39m")


if __name__ == '__main__':
    unittest.main()
