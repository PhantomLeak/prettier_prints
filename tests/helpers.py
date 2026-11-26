import unittest


class VisualTestCase(unittest.TestCase):
    def show(self, *args, **kwargs):
        """Print visual output for manual inspection.

        No-op by default; tests/conftest.py replaces it when running `pytest --output`.
        """
