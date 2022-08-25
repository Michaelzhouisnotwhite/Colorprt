# Display mode
from enum import Enum


class Mode(Enum):
    DEFAULT = 0
    BOLD = 1
    UNDER_LINE = 4
    FLASH = 5
    REVERSE = 7

    # @classmethod
    # def range(cls):
    #     return [cls.DEFAULT, cls.BOLD, cls.UNDER_LINE, cls.FLASH, cls.REVERSE]


class Fore(Enum):
    DEFAULT = 0
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    # @classmethod
    # def range(cls):
    #     return [i for i in range(cls.BLACK, cls.WHITE + 1)] + [cls.DEFAULT]


class Back(Enum):
    DEFAULT = 0
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47

    # @classmethod
    # def range(cls):
    #     return [i for i in range(cls.BLACK, cls.WHITE + 1)] + [cls.DEFAULT]
