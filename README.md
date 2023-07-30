# Prettier_prints

Lightweight library for prettier terminal outputs

ex usage 
```bash
    from prettier_prints.prettier_prints import PrettierPrints
    prints = PrettierPrints()

    prints.output_message(color_one=prints.red, msg='This is a test',
                          color_two=prints.green, output='The test worked')
```