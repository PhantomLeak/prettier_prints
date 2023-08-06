from prettier_prints.prettier_prints import PrettierPrints

prettier_prints = PrettierPrints()


def test_print():
    prettier_prints.style = 'yellow;bold;underline'
    assert print(f'This is a test -> {prettier_prints.out(msg="This is an assert test")}')
    assert print(f'This is a test -> {prettier_prints.out(msg="This is an assert test", style="red;bold")}')
    assert print(f'This is a test -> {prettier_prints.out(json_out={"msg": "test test", "style": "blue"})}')

