from prettier_prints.ansi_styling import Colors, Decorators


class Output(Colors, Decorators):
    def __init__(self, message: str = ''):
        super().__init__(message)

    def __str__(self):
        return f"{self.output_message}"

    def msg(self, message: str) -> 'Output':
        # Return a new object so pp itself is never mutated
        return Output(message)

    # return the output message
    def out(self) -> str:
        return f'{self.output_message}'
