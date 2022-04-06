# solve the n-queens by using backtracking

def create_grid(n: int) -> list:
    return [[0] * n for _ in range(n)]


def print_grid(grid: list) -> None:
    for row in grid:
        for column in row:
            print(column, end=" ")
        print("", end="\n")

    
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


def solutions(grid: list, i: int=0) -> int:
    n = len(grid)
    if i == n:
        return 1
    else:
        counter = 0
        for j in range(n):
            if is_safe(grid, i, j):
                grid[i][j] = 1
                counter += solutions(grid, i+1)
                grid[i][j] = 0
        return counter


def n_queens(n: int) -> int:
    return solutions(create_grid(n))


if __name__ == "__main__":
    n = 8
    print(f"for n={n} -> {n_queens(n)}")
