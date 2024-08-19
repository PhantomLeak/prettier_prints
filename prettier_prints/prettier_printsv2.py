from prettier_prints.ansi_styling import Colors, Decorators


class Output(Colors, Decorators):
    def __init__(self):
        self.output_message: str = ''
        super().__init__(self.output_message)

    def __str__(self):
        return f"{self.output_message}"

    def msg(self, message: str):
        self.output_message: str = message
        return self

    # return the output message
    def out(self) -> str:
        return f'{self.output_message}'

