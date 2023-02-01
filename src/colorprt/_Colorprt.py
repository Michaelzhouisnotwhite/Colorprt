from typing import Any, List, Tuple, Union
from ._vars import *

SC = '\033['
EC = '\033[0m'


def colorprt(*args, **kwargs):
    """
    It's a printing function

    Usage:
        from colorprt import colorprt, Back, Fore

        colorprt("Hello World", Back.RED)
    """
    config_list = []
    output_string = []
    for arg in list(args):
        if isinstance(arg, (Fore, Back, Mode)):
            config_list.append(arg)

        else:
            output_string.append(arg)
    ColorprtConfig(*config_list).print(*output_string, **kwargs)


class _ColorStr:
    start = SC
    end = EC

    def __init__(self, s=SC, e=EC):
        self.start = s
        self.end = e

    def combine(self, *output: Any):
        res_string = f"{list(output)[0]}"
        for arg in list(output)[1:]:
            res_string += f" {arg}"
        return f"{self.start}{res_string}{self.end}"


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

    def print(self, *outputs: Any, **kwargs):
        print(self.preprocess_color_prefix().combine(*outputs), **kwargs)

    def copy(self):
        return ColorprtConfig(*self.arg_list)

    @property
    def config_list(self):
        return [self.background, self.foreground, self.mode]

    def __call__(self, *plain_string: Any) -> str:
        return self.preprocess_color_prefix().combine(*plain_string)


class _Colorprt(ColorPtrBase):
    def __init__(self, plain_string: str, *args: Union[Union[Mode, Back, Fore], ColorprtConfig]):
        self.output = plain_string
        self.color_config = None
        for param in list(args):
            if isinstance(param, ColorprtConfig):
                self.color_config = param.copy()
                super().__init__(*self.color_config.config_list)
                break
        if self.color_config is None:
            super().__init__(*args)
        else:
            for param in list(args):
                if isinstance(param, Mode):
                    self.mode = param
                if isinstance(param, Back):
                    self.background = param
                if isinstance(param, Fore):
                    self.foreground = param

    def __str__(self):
        return self.preprocess_color_prefix().combine(self.output)

    def str(self):
        return self.preprocess_color_prefix().combine(self.output)

    def __add__(self, other: Any):
        return _Colorprt(str(self) + str(other))
