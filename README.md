# Prettier_prints

Lightweight library for prettier terminal outputs similar to [chalk](https://github.com/chalk/chalk) for JavaScript. 
Helping make Python outputs easier to read and styled to your desires.

### Install
```python
pip install prettier-prints
```

Example:
```python
    from prettier_prints.prettier_prints import PrettierPrints
    pp = PrettierPrints()
    pp.style = 'red;underline'  # <-- Can optionally predefine styling and can be overwritten

    print(pp.out(msg="Lets test the output"))
    print(pp.out(msg="Lets override the styling here", style="blue;bold"))
    print(pp.out(json_out={'msg': 'For those who prefer a JSON object param, this works too'}))
    print(pp.out(json_out={'msg': 'Can also overwrite this way', 'style': 'yellow;highlight'}))
    print(f'Works great for output messages as well -> {pp.out(msg="See :)", style="magenta")}')
```
![output image](https://github.com/PhantomLeak/prettier_prints/blob/main/print_output.png?raw=true)

### Current functions:
 - out()

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

