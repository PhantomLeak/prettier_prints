from prettier_prints.myfunctions import Colors

colors = Colors()


def test_print():
    assert colors.print(color='red', message='This is a test')


def test_output_msg():
    assert colors.output_message(color_one='green', msg='This is a test',
                                 output='Success')
