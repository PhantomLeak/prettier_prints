# Prettier_prints

Lightweight library for prettier terminal outputs similar to [chalk](https://github.com/chalk/chalk) for JavaScript. 
Helping make Python outputs easier to read and styled to your desires.

### Install
```python
pip install prettier-prints
```

Examples:
out() 
```python
    from prettier_prints.prettier_prints import PrettierPrints
    pp = PrettierPrints()
    pp.style = 'red;underline'  # <-- Can optionally predefine styling and can be overwritten
    
    # Old style (v1)
    print(pp.out(msg="Lets test the output"))
    print(pp.out(msg="Lets override the styling here", style="blue;bold"))
    print(pp.out(json_out={'msg': 'For those who prefer a JSON object param, this works too'}))
    print(pp.out(json_out={'msg': 'Can also overwrite this way', 'style': 'yellow;highlight'}))
    print(f'Works great for output messages as well -> {pp.out(msg="See :)", style="magenta")}')

    # New v2 style
    from prettier_prints.prettier_printsv2 import Output
    pp = Output()
    print(f"\n{pp.msg('Hello').red().bold().underline()}")
    print(f"{pp.msg('Hello').green().bold().out()}")
```
![output image](https://github.com/PhantomLeak/prettier_prints/blob/main/print_output.png?raw=true)

json()
```python
    from prettier_prints.prettier_prints import PrettierPrints
    pp = PrettierPrints()
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
    print(prettier_prints.json(json_obj=json_obj, style='list=blue;underline&dict=red;bold&string=green;'))
```
![output image](https://github.com/PhantomLeak/prettier_prints/blob/main/json_output.png?raw=true)

### Current functions:
 - out()
 - json()

### Function parameters:
     - out()
       - msg: str           Output / display message[required]
       - style: str         Styling to apply to the message[optional]
       - json_out: dict     JSON object containing the message and styling[optional]

     - json()
       - style: str         Styling to apply to the message[optional]
       - json_obj: dict     JSON object containing the message and styling[required]
 
### Styling Examples By Function (v1 style):
    - out()
        - style: 'red;underline'
        - json_out: {'msg': 'Lets test the output', 'style': 'blue;bold'}
    - json()
        - style: 'list=red;underline&dict=blue;bold&str=yellow;highlight' # <- Break up the styling by type (list, dict, str)

### Current available styling:
| Modifiers | Colors / Background Colors |    
|:----------|:--------------------------:|
| Bold      |            Red             |
| Underline |           Green            | 
| Highlight |           Yellow           |
|           |            Blue            |
|           |          Magenta           |
|           |            Cyan            |
|           |           White            |
|           |         Bright Red         |
|           |        Bright Green        |
|           |       Bright Yellow        |
|           |        Bright Blue         |
|           |       Bright Magenta       |
|           |        Bright Cyan         |
|           |        Bright White        |

### Contributors / Thanks:
 - [SheepDogg586](https://github.com/SheepDogg586)

