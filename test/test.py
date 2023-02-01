from colorprt import colorstr, ColorprtConfig, Fore, Mode, Back, colorprt
from colorprt.default import warn_color, success_color, error_color

pycolor_config = ColorprtConfig(Back.RED, Fore.DEFAULT)
pycolor_config.print("I love You!!", "I love China as well", end="\n\n")

lang_output_config = ColorprtConfig(Fore.BLUE, Back.YELLOW)
a = colorstr('asdfasdf', lang_output_config)
print(a)

pycolor_config = ColorprtConfig(Back.DEFAULT, Fore.RED, Mode.BOLD)
pycolor_config.print("I hate You!!", a, end="")

b = colorstr("this is a hate string", pycolor_config, Back.YELLOW)
c = colorstr("this is another hate string", pycolor_config, Fore.CYAN, Back.RED, Mode.BOLD)

print(c + " " + b)
print(f"format string test: {b + c}")

# test exception

try:
    ColorprtConfig(Back.DEFAULT, Fore.RED, Mode.BOLD, "invalid arg")

except TypeError as e:
    error_color.print(e, end="\n\n")
    warn_color.print(e)
    print(success_color(e))

colorprt("dafj", "eaifjaejf", b, f"{c}", end=" ####\n")

