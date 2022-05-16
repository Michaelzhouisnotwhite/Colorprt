from ._vars import *

SC = '\033['
EC = '\033[0m'


def clrprint(*args, **kwargs):
    print(_PyColorPrint(*args, **kwargs))


class PyColorConfig:
    def __init__(self, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT):
        self.mode = mode
        if foreground == Fore.DEFAULT:
            self.foreground = ''
        else:
            self.foreground = ';' + str(foreground)
        if background == Back.DEFAULT:
            self.background = ''
        else:
            self.background = ';' + str(background)

    def __call__(self, output: str):
        print(_PyColorPrint(output, self.mode, self.foreground, self.background))


class _PyColorPrint:
    def __init__(self, output: str, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT,
                 config: PyColorConfig = None):
        if config is not None:
            self.foreground = config.foreground
            self.background = config.background
            self.mode = config.mode

        self.output = output
        self.mode = mode
        if foreground == Fore.DEFAULT:
            self.foreground = ''
        else:
            self.foreground = ';' + str(foreground)
        if background == Back.DEFAULT:
            self.background = ''
        else:
            self.background = ';' + str(background)

    def __str__(self):
        return f'{SC}{self.mode}{self.foreground}{self.background}m{self.output}{EC}'

    def str(self):
        return f'{SC}{self.mode}{self.foreground}{self.background}m{self.output}{EC}'

    def __add__(self, other):
        return _PyColorPrint(str(self) + str(other))
