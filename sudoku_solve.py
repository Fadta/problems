SUDOKU_LENGTH = 9
SUDOKU_SUBGRID_LENGTH = 3


def create_sudoku_grid():
    return [[0] * SUDOKU_LENGTH for _  in range(SUDOKU_LENGTH)]


def print_sudoku_grid(sudoku:list[list[int]]):
    for i in range(SUDOKU_LENGTH):
        for j in range(SUDOKU_LENGTH):
            print(sudoku[i][j], end=" ")
            if j != 8 and ((j + 1) % SUDOKU_SUBGRID_LENGTH) == 0:
                print("|", end=" ")
        print(end="\n")
        if i != 8 and ((i + 1) % SUDOKU_SUBGRID_LENGTH) == 0:
            print("-----------------------")


def valid_placing(sudoku:list[list[int]], r:int, c:int, k:int) -> bool:
    in_row = k in sudoku[r]
    if(not in_row):
        in_column = k in [sudoku[r][col] for col in range(SUDOKU_LENGTH)]
        if(not in_column):
            subgrid_r = r//SUDOKU_SUBGRID_LENGTH
            subgrid_c = c//SUDOKU_SUBGRID_LENGTH
            in_subgrid = k in [sudoku[row][col] for row in range(subgrid_r * 3, (subgrid_r+1) * 3) for col in range(subgrid_c*3, (subgrid_c+1) * 3)]
            # precondition: not in_row and not in_column
            return not in_subgrid
    return False


def solve(sudoku:list[list[int]], r:int=0, c:int=0) -> bool:
    if c == SUDOKU_LENGTH:
        return solve(sudoku, r+1, 0)
    elif r == SUDOKU_LENGTH:
        return True
    elif sudoku[r][c] != 0:
        return solve(sudoku, r, c+1)
    else:
        for k in range(1, 10):
            if valid_placing(sudoku, r, c, k):
                sudoku[r][c] = k
                if (solve(sudoku, r, c+1)):
                    return True
                sudoku[r][c] = 0
        return False

def sudoku_sample(sudoku:list[list[int]]) -> None:
    sudoku[1][5] = 3
    sudoku[1][7] = 8
    sudoku[1][8] = 5

    sudoku[2][2] = 1
    sudoku[2][4] = 2

    sudoku[3][3] = 5
    sudoku[3][5] = 7

    sudoku[4][2] = 4
    sudoku[4][6] = 1

    sudoku[5][1] = 9

    sudoku[6][0] = 5
    sudoku[6][7] = 7
    sudoku[6][8] = 3

    sudoku[7][2] = 2
    sudoku[7][4] = 1

    sudoku[8][4] = 4
    sudoku[8][8] = 9


if __name__ == "__main__":
    sudoku = create_sudoku_grid()

    sudoku_sample(sudoku)
    print_sudoku_grid(sudoku)
    print("\n")

    solve(sudoku)
    print_sudoku_grid(sudoku)
