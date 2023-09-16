from prettier_prints.prettier_prints import PrettierPrints

prettier_prints = PrettierPrints()


def test_print():
    prettier_prints.style = 'yellow;bold;underline'
    assert print(f'This is a test -> {prettier_prints.out(msg="This is an assert test")}')
    assert print(f'This is a test -> {prettier_prints.out(msg="This is an assert test", style="red;bold")}')
    assert print(f'This is a test -> {prettier_prints.out(json_out={"msg": "test test", "style": "blue"})}')


def test_json_print():
    json_obj = {'test': 'cool', 'test_two': 'cool_two', 'dict_check': {'test': 'hello'},
                'list_check': [
                    'test',
                    'test two',
                    {
                        'test': 'hello',
                        'test_two': 'bloop'
                    },
                    {
                        'test': 'hello',
                        'test_two': 'bloop'
                    }
                ]}
    assert print(prettier_prints.json(json_obj=json_obj, style='list=blue;underline&dict=red;bold&string=green;'))
