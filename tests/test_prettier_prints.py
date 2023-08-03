from prettier_prints.prettier_prints import PrettierPrints

prettier_prints = PrettierPrints()


def test_print():
    assert print(f'This is a test -> {prettier_prints.out(print_msg={"msg": " and it works", "style": "blue;bold;underline"})}')

