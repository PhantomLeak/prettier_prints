# Prettier_prints

Lightweight library for prettier terminal outputs similar to [chalk](https://github.com/chalk/chalk) for JavaScript. 
Helping make Python outputs easier to read and styled to your desires.

### Install
```python
pip install prettier-prints
```

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


Example:
```python
    from prettier_prints.prettier_prints import PrettierPrints
    pp = PrettierPrints()
    print(pp.out({'msg': "Let's turn this message red", 'style': 'red'}))
    print(pp.out({'msg': "Lets also underline it", 'style': 'red;underline'}))
    print(pp.out({'msg': "May as well bold it too", 'style': 'red;underline;bold'}))
    print(pp.out({'msg': "What about a blue background?", 'style': 'blue;highlight'}))
    print(f'This also works for output messages -> {pp.out(print_msg={"msg": "See :)", "style": "magenta;bold;underline"})}')
```
![output image](https://github.com/PhantomLeak/prettier_prints/blob/main/Screenshot%20from%202023-08-02%2023-48-41.png?raw=true)
