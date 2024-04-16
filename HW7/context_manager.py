class colorize:
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        print(self.COLORS[self.color], end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.COLORS['reset'], end='')


with colorize('red'):
    print("This text will be printed in red")

print("This text will be printed in the default color")
