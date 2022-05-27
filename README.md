# Colorprt

It's a simple package for you to customize the printing color.

pypi: <https://pypi.org/project/colorprt/>

## New Features

We add some default default color config in out package.

```python
from colorprt.default import warn, success, error

warn("Print a warn message")
success("Print a success message")
error("Print an error message")
```

We found that some people use this package on linux server, so that there is no auto completions. It will trouble users.
Therefore, we add a feature that
You don't need to type: `mode=`; `foreground=`; `background=`

just call functions or class like this:

In old versions:

```python
from colorprt import colorprt, Back, Fore

colorprt("Hello World", backgound=Back.RED)
```

Use new features:

```python
from colorprt import colorprt, Back, Fore

colorprt("Hello World", Back.RED)
```

## Usage

```bash
pip install colorprt
```

function colorprt will automatically call output function: `print`

```python
from colorprt import colorprt, Back, Fore

colorprt("Hello World", Back.RED)
```

- Back stands for background;
- Fore stands for foreground;
- Mode stands for printing mode. ( font style like: underline, bold, flash, reverse )

Also, you can use a config class to set colored strings.

```python
from colorprt import ColorprtConfig, Mode, Back, Fore

pycolor_config = ColorprtConfig(mode=Mode.BOLD, background=Back.DEFAULT, foreground=Fore.RED)
pycolor_config("I love You!!", end="")
```

If you just want the ansi colored formatted strings, you can use `colorstr` class.

```python
from colorprt import colorstr, Mode, Back, Fore, ColorprtConfig

hate_print_config = ColorprtConfig(mode=Mode.UNDER_LINE, background=Back.DEFAULT, foreground=Fore.YELLOW)
print(colorstr("I love You!!", mode=Mode.BOLD, background=Back.DEFAULT, foreground=Fore.RED)
      + colorstr("I hate you", config=hate_print_config))
```

if you use str() to force change to string. You will get

```
>>> str(colorstr("I love You!!", mode=Mode.BOLD, background=Back.DEFAULT, foreground=Fore.RED)
      + colorstr("I hate you", config=hate_print_config))
>>> '\x1b[0m\x1b[1;31mI love You!!\x1b[0m\x1b[4;33mI hate you\x1b[0m\x1b[0m'
```

Therefore, if you just want the strings with ANSI formatted.

```python
from colorprt import colorstr, Mode, Back, Fore, ColorprtConfig

hate_print_config = ColorprtConfig(mode=Mode.UNDER_LINE, background=Back.DEFAULT, foreground=Fore.YELLOW)

output = str(colorstr('I hate You', config=hate_print_config))
```


