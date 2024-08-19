import unittest
from prettier_prints.prettier_printsv2 import Output


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.prettier_prints = Output()

    def test_something(self):
        print(f"\n{self.prettier_prints.msg('Hello').red().bold().underline()}")
        print(f"{self.prettier_prints.msg('Hello').green().bold().out()}")
        print(f"{self.prettier_prints.msg('Hello').yellow().underline().out()}")
        print(f"{self.prettier_prints.msg('Hello').blue().out()}")
        print(f"{self.prettier_prints.msg('Hello').magenta().bold().highlight()}")


if __name__ == '__main__':
    unittest.main()
