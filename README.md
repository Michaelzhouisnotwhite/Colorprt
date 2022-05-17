# Colorprt

It's a simple package for you to customize the printing color.

## Usage

```bash
pip install colorprt
```

```python
from colorprt import colorprt, Back, Fore

colorprt("Hello World", background=Back.RED)
```

Back stands for background;Fore stands for foreground

Also, you can use a config class to print colored strings.

```python
from colorprt import ColorprtConfig, Mode, Back, Fore

pycolor_config = ColorprtConfig(mode=Mode.BOLD, background=Back.DEFAULT, foreground=Fore.RED)
pycolor_config("I love You!!", end="")
```

If you just want the ansi colored formatted strings, you can use `clrstr` class.

```python
from colorprt import clrstr, Mode, Back, Fore, ColorprtConfig

hate_print_config = ColorprtConfig(mode=Mode.UNDER_LINE, background=Back.DEFAULT, foreground=Fore.YELLOW)
print(clrstr("I love You!!", mode=Mode.BOLD, background=Back.DEFAULT, foreground=Fore.RED)
      + clrstr("I hate you", hate_print_config))
```


