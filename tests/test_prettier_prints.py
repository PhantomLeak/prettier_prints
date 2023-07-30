from prettier_prints.prettier_prints import PrettierPrints

prettier_prints = PrettierPrints()


def test_print():
    assert prettier_prints.print(color='red', message='This is a test', bold_text=True)


def test_output_msg():
    assert prettier_prints.output_message(color_one='green', msg='This is a test',
                                          output='Success')

