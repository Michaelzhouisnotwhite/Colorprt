from ._vars import *

SC = '\033['
EC = '\033[0m'


def colorprt(*args, **kwargs):
    print(_Colorprt(*args, **kwargs))


class Str:
    start = SC
    end = EC

    def __init__(self, s=SC, e=EC):
        self.start = s
        self.end = e

    def combine(self, output: str):
        output = str(output)
        return self.start + output + self.end


class Base:
    def __init__(self, *args, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT, **kwargs):
        self.mode = mode
        self.foreground = foreground
        self.background = background
        if args:
            for arg in list(args):
                if arg in Fore.range():
                    self.foreground = arg
                elif arg in Back.range():
                    self.background = arg
                elif arg in Mode.range():
                    self.mode = arg

    def preprocess_color_str(self):
        if self.foreground == Fore.DEFAULT:
            foreground = ''
        else:
            foreground = ';' + str(self.foreground)
        if self.background == Back.DEFAULT:
            background = ''
        else:
            background = ';' + str(self.background)
        return Str(s=f'{SC}{self.mode}{foreground}{background}m')


class ColorprtConfig(Base):
    def __init__(self, *args, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT, **kwargs):
        super().__init__(*args, mode=mode, foreground=foreground, background=background, **kwargs)

    def __call__(self, output: str, **kwargs):
        print(self.preprocess_color_str().combine(output), **kwargs)


class _Colorprt(Base):
    def __init__(self, output: str, *args, mode=Mode.DEFAULT, foreground=Fore.DEFAULT, background=Back.DEFAULT,
                 config: ColorprtConfig = None):
        if config is not None:
            super(_Colorprt, self).__init__(*args, mode=config.mode, foreground=config.foreground,
                                            background=config.background)
        else:
            super().__init__(*args, mode=mode, foreground=foreground, background=background)

        self.output = output

    def __str__(self):
        return self.preprocess_color_str().combine(self.output)

    def str(self):
        return self.preprocess_color_str().combine(self.output)

    def __add__(self, other):
        return _Colorprt(str(self) + str(other))
