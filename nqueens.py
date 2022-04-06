import time
import utils as u
# solve the n-queens by using backtracking
SLEEP_TIME = 0
SUCCESS_TIME = 0.25

def create_grid(n: int) -> list:
    return [[0] * n for _ in range(n)]


def print_grid(grid: list, solutions: int) -> None:
    for r in grid:
        for c in r:
            if c == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print(end="\n")
    print("Solutions found -> ", solutions)
    time.sleep(SLEEP_TIME)
    u.cursor_up(9)


def print_completed(grid: list, solutions: int) -> None:
    print("\033[42m", end="")
    for r in grid:
        for c in r:
            char = "Q" if c == 1 else "-"
            print(char, end=" ")
        print(end="\n")
    print("\033[0m", end="")
    print("Solutions found -> ", solutions)
    time.sleep(SUCCESS_TIME)
    u.cursor_up(9)


def print_wrong(grid: list, i:int, j:int, solutions: int) -> None:
    n = len(grid)
    for r in range(n):
        for c in range(n):
            char = "Q" if grid[r][c] == 1 else "-"
            if i == r and j == c:
                print("\033[31mQ\033[0m", end=" ")
            else:
                print(char, end=" ")
        print(end="\n")
    print("Solutions found -> ", solutions)
    time.sleep(SLEEP_TIME)
    u.cursor_up(9)
    

    
def is_safe(grid: list, i: int, j: int) -> bool:
    n = len(grid)
    j_left = j
    j_right = j
    while i >= 0:
        if ((j_left >= 0 and grid[i][j_left])
        or grid[i][j]
        or (j_right < n and grid[i][j_right])):
            return False
        i -= 1
        j_right += 1
        j_left -= 1
    return True


def solutions(grid: list, i: int=0, count: int=0) -> int:
    n = len(grid)
    if i == n:
        print_completed(grid, count)
        return 1
    else:
        counter = 0
        for j in range(n):
            if is_safe(grid, i, j):
                grid[i][j] = 1
                print_grid(grid, count)
                counter += solutions(grid, i+1, counter)
                grid[i][j] = 0
                print_grid(grid, count)
            else:
                print_wrong(grid, i, j, count)
        return counter


def n_queens(n: int) -> int:
    return solutions(create_grid(n))


if __name__ == "__main__":
    n = 8
    print(f"solutions for n={n} -> {n_queens(n)}")
