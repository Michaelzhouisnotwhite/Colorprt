from typing import List, Union
from ._vars import *

SC = '\033['
EC = '\033[0m'


def colorprt(*args, **kwargs):
    print(_Colorprt(*args), **kwargs)


class _ColorStr:
    start = SC
    end = EC

    def __init__(self, s=SC, e=EC):
        self.start = s
        self.end = e

    def combine(self, output: str):
        output = str(output)
        return self.start + output + self.end


class ColorPtrBase:
    def __init__(self, *args):
        self.mode: Mode = Mode.DEFAULT
        self.foreground: Fore = Fore.DEFAULT
        self.background: Back = Back.DEFAULT
        if args:
            for arg in list(args):
                if isinstance(arg, Fore):
                    self.foreground = arg
                elif isinstance(arg, Back):
                    self.background = arg
                elif isinstance(arg, Mode):
                    self.mode = arg

                else:
                    raise TypeError(f"{arg} is an invalid arguments.")

    def preprocess_color_prefix(self):
        if self.foreground == Fore.DEFAULT:
            foreground = ''
        else:
            foreground = ';' + str(self.foreground.value)
        if self.background == Back.DEFAULT:
            background = ''
        else:
            background = ';' + str(self.background.value)
        return _ColorStr(s=f'{SC}{self.mode.value}{foreground}{background}m')


class ColorprtConfig(ColorPtrBase):
    def __init__(self, *args):
        self.arg_list = args
        super().__init__(*args)

    def print(self, output_string: str, **kwargs):
        print(self.preprocess_color_prefix().combine(output_string), **kwargs)

    def copy(self):
        return ColorprtConfig(*self.arg_list)

    @property
    def config_list(self):
        return [self.background, self.foreground, self.mode]


class _Colorprt(ColorPtrBase): 
    def __init__(self, plain_string: str, *args: Union[List[Union[Mode, Back, Fore]], List[ColorprtConfig]]):
        self.output = plain_string
        self.color_config = None
        for parm in list(args):
            if isinstance(parm, ColorprtConfig):
                self.color_config = parm.copy()
                super().__init__(*self.color_config.config_list)
                break
        if self.color_config is None:
            super().__init__(*args)
        else:
            for parm in list(args):
                if isinstance(parm, Mode):
                    self.mode = parm
                if isinstance(parm, Back):
                    self.background = parm
                if isinstance(parm, Fore):
                    self.foreground = parm

    def __str__(self):
        return self.preprocess_color_prefix().combine(self.output)

    def str(self):
        return self.preprocess_color_prefix().combine(self.output)

    def __add__(self, other):
        return _Colorprt(str(self) + str(other))
