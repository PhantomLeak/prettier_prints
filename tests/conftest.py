import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--output",
        action="store_true",
        default=False,
        help="Display the visual output (color swatches, nested styles, JSON) printed by the tests.",
    )


@pytest.fixture(autouse=True)
def _visual_output(request):
    """Give each test a show() that prints only when `pytest --output` is used.

    Output bypasses pytest's capture (no -s needed), so it appears even for passing tests.
    """
    if not request.config.getoption("output"):
        return  # VisualTestCase.show stays a no-op

    capsys = request.getfixturevalue("capsys")

    def show(*args, **kwargs):
        with capsys.disabled():
            print(*args, **kwargs)

    if request.instance is not None:
        request.instance.show = show
