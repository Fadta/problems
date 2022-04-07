from enum import Enum


class ANSIColor:
    def __init__(self) -> None:
        self.RESET = "\033[0m"

        self.FG_BLACK = "\033[30m"
        self.FG_RED = "\033[31m"
        self.FG_GREEN = "\033[32m"
        self.FG_YELLOW = "\033[33m"
        self.FG_BLUE = "\033[34m"
        self.FG_MAGENTA = "\033[35m"
        self.FG_CYAN = "\033[36m"
        self.FG_WHITE = "\033[37m"
        self.FG_BRIGHT_BLACK = "\033[90m"
        self.FG_BRIGHT_RED = "\033[91m"
        self.FG_BRIGHT_GREEN = "\033[92m"
        self.FG_BRIGHT_YELLOW = "\033[93m"
        self.FG_BRIGHT_BLUE = "\033[94m"
        self.FG_BRIGHT_MAGENTA = "\033[95m"
        self.FG_BRIGHT_CYAN = "\033[96m"
        self.FG_BRIGHT_WHITE = "\033[97m"

        self.BG_BLACK = "\033[40m"
        self.BG_RED = "\033[41m"
        self.BG_GREEN = "\033[42m"
        self.BG_YELLOW = "\033[43m"
        self.BG_BLUE = "\033[44m"
        self.BG_MAGENTA = "\033[45m"
        self.BG_CYAN = "\033[46m"
        self.BG_WHITE = "\033[47m"
        self.BG_BRIGHT_BLACK = "\033[100m"
        self.BG_BRIGHT_RED = "\033[101m"
        self.BG_BRIGHT_GREEN = "\033[102m"
        self.BG_BRIGHT_YELLOW = "\033[103m"
        self.BG_BRIGHT_BLUE = "\033[104m"
        self.BG_BRIGHT_MAGENTA = "\033[105m"
        self.BG_BRIGHT_CYAN = "\033[106m"
        self.BG_BRIGHT_WHITE = "\033[107m"


    @staticmethod
    def fg_rgb(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"


    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{g};{b}m"


def cursor_up(n: int) -> None:
    print(f"\033[{n}A", end="\r")


def cursor_down(n: int) -> None:
    print(f"\033[{n}B")


def cursor_right(n: int) -> None:
    print(f"\033[{n}C")


def cursor_left(n: int) -> None:
    print(f"\033[{n}D")


def cursor_line_down(n: int) -> None:
    print(f"\033[{n}E")


def cursor_line_up(n: int) -> None:
    print(f"\033[{n}F")
