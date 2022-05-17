from colorprt import colorstr, ColorprtConfig, Fore, Mode, Back

lang_output_config = ColorprtConfig(foreground=Fore.BLUE)
a = str(colorstr('asdfasdf', config=lang_output_config))
print(a)

pycolor_config = ColorprtConfig(background=Back.DEFAULT, foreground=Fore.RED)
pycolor_config("I love You!!", end="")
pass

