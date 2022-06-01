from colorprt import colorstr, ColorprtConfig, Fore, Mode, Back

lang_output_config = ColorprtConfig(Fore.BLUE, Back.YELLOW)
a = colorstr('asdfasdf', config=lang_output_config)
print(a)

pycolor_config = ColorprtConfig(Back.RED, foreground=Fore.DEFAULT)
pycolor_config("I love You!!", end="\n\n")

pycolor_config = ColorprtConfig(Back.DEFAULT, Fore.RED, Mode.BOLD)
pycolor_config("I hate You!!", end="")
