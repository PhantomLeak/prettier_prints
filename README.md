# Prettier_prints

Lightweight library for prettier terminal outputs

Current functions:
 - print()
 - output_message() 

Example:
```python
from prettier_prints.prettier_prints import PrettierPrints
prettier_prints = PrettierPrints()

prettier_prints.print(color=prettier_prints.magenta, message='test')

prettier_prints.output_message(color_one=prettier_prints.red, msg='This is a test',
                               color_two=prettier_prints.green, output='The test worked')
```
<img src="assets/print_output.png" height="50" height="50" alt="outputImage">
