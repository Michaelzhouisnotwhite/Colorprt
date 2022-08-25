from colorprt import colorstr, ColorprtConfig, Fore, Mode, Back

pycolor_config = ColorprtConfig(Back.RED, Fore.DEFAULT)
pycolor_config.print("I love You!!", end="\n\n")

lang_output_config = ColorprtConfig(Fore.BLUE, Back.YELLOW)
a = colorstr('asdfasdf', lang_output_config)
print(a)

pycolor_config = ColorprtConfig(Back.DEFAULT, Fore.RED, Mode.BOLD)
pycolor_config.print("I hate You!!", end="")

b = colorstr("this is a hate string", pycolor_config, Back.YELLOW)
c = colorstr("this is anothor hate string", pycolor_config, Fore.CYAN, Back.RED, Mode.BOLD)

print(c + " " + b)
print(f"format string test: {b + c}")

### test exception
ColorprtConfig(Back.DEFAULT, Fore.RED, Mode.BOLD, 123)
