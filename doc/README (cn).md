# Colorprt

[English](../README.md) | [中文](./README%20(cn).md)

这是一个简单的软件包，您可以自定义控制台打印颜色。

pypi: <https://pypi.org/project/colorprt/>

## 截图

<img alt="img.png" src="https://github.com/Michaelzhouisnotwhite/Colorprt/blob/main/.github/img.png?raw=true" style="width: 760px;text-align: center"/>

## 新特性

我们在包中添加了一些默认颜色配置。

```python
from colorprt.default import warn_color, success_color, error_color

warn_color.print("Print a warn message")
success_color.print("Print a success message")
error_color.print("Print an error message")
```

我们发现有些人在linux服务器上使用这个包，所以没有自动完成。这会给用户带来麻烦。因此，我们添加了一个不需要输入的特性： `mode=`; `foreground=`; `background=`

只需要这么调用：

在旧的版本中：

```python
from colorprt import colorprt, Back, Fore

# 警告：不要在版本3.0.0之后使用此功能
colorprt("Hello World", backgound=Back.RED)
```

使用新的特性：

```python
from colorprt import colorprt, Back, Fore

colorprt("Hello World", Back.RED, Fore.YELLOW)
```

## 使用方法

### 安装

```bash
pip install colorprt
```

### 详细文档

函数 `colorprt` 是一个 `print` 函数的扩展。 你可以自定义打印输出的颜色。

```python
from colorprt import colorprt, Back, Fore

hello_else = "Hello Michael"
colorprt("Hello World",hello_else,  Back.RED, Fore.BLUE end="x100 times\n")
```
![scshots01](https://github.com/Michaelzhouisnotwhite/Colorprt/blob/main/.github/scshots01.png?raw=true)

- Back 是背景色;
- Fore 是前景色;
- Mode 是字体样式. ( underline, bold, flash, reverse )

不仅如此，你可以使用 `ColorprtConfig` 类来预先保存设定的颜色.

```python
from colorprt import ColorprtConfig, Mode, Back, Fore

pycolor_config = ColorprtConfig(Mode.BOLD, Back.DEFAULT, Fore.RED)

#你可以使用ColorprtConfig 字符串的配置颜色

colored_formatted_str = pycolor_config("I love You!!")

print(colored_formatted_str)

# or just use print method

pycolor_config.print("I love you!!", end="x10086\n")
```

如果您只需要ansi彩色格式的字符串，可以使用'colorstr'类。

```python
from colorprt import colorstr, Mode, Back, Fore, ColorprtConfig

hate_print_config = ColorprtConfig(Mode.UNDER_LINE, Back.DEFAULT, Fore.YELLOW)
print(colorstr("I love You!!", Mode.BOLD, Back.DEFAULT, Fore.RED)
      + colorstr("I hate you", hate_print_config))
```

如果使用str（）强制更改字符串来查看字符串内容。你会得到

```
>>> str(colorstr("I love You!!", Mode.BOLD, Back.DEFAULT, Fore.RED)
      + colorstr("I hate you", hate_print_config))
>>> '\x1b[0m\x1b[1;31mI love You!!\x1b[0m\x1b[4;33mI hate you\x1b[0m\x1b[0m'
```


```python
from colorprt import colorstr, Mode, Back, Fore, ColorprtConfig

hate_print_config = ColorprtConfig(Mode.UNDER_LINE, Back.DEFAULT, Fore.YELLOW)

output = str(colorstr('I hate You', hate_print_config))
```


