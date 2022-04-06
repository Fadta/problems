def cursor_up(n: int) -> None:
    print(f"\033[{n}A", end="\r")
