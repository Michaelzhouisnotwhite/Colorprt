from ._vars import *

SC = '\033['
EC = '\033[0m'


def colorprt(*args, **kwargs):
    print(_Colorprt(*args, **kwargs))


class ColorprtConfig:
    def __init__(self, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT, **kwargs):
        self.mode = mode
        if foreground == Fore.DEFAULT:
            self.foreground = ''
        else:
            self.foreground = ';' + str(foreground)
        if background == Back.DEFAULT:
            self.background = ''
        else:
            self.background = ';' + str(background)

    def __call__(self, output: str, **kwargs):
        print(_Colorprt(output, config=self), **kwargs)


class _Colorprt:
    def __init__(self, output: str, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT,
                 config: ColorprtConfig = None):
        self.output = output

        if config is not None:
            self.foreground = config.foreground
            self.background = config.background
            self.mode = config.mode
        else:
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
        return _Colorprt(str(self) + str(other))
