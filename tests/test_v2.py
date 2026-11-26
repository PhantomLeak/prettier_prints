import unittest
from prettier_prints.prettier_printsv2 import Output


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

    def test_existing_escape_output_unchanged(self):
        # Escape codes are untouched by this fix (bugs 2/3 will change them later)
        self.assertEqual(str(self.pp.msg('Hi').red()), "\033[31mHi\033[0m")
        self.assertEqual(str(self.pp.msg('Hi').yellow().bold()), "\033[1m\033[33mHi\033[0m\033[0m")


if __name__ == '__main__':
    unittest.main()
