SUDOKU_LENGTH = 9
SUDOKU_SUBGRID_LENGTH = 3
def create_sudoku_grid():
    return [[0] * SUDOKU_LENGTH for _  in range(SUDOKU_LENGTH)]

def print_sudoku_grid(sudoku: list[list[int]]):
    for i in range(SUDOKU_LENGTH):
        for j in range(SUDOKU_LENGTH):
            print(sudoku[i][j], end=" ")
            if j != 8 and ((j + 1) % SUDOKU_SUBGRID_LENGTH) == 0:
                print("|", end=" ")
        print(end="\n")
        if i != 8 and ((i + 1) % SUDOKU_SUBGRID_LENGTH) == 0:
            print("-----------------------")


def is_valid(sudoku:list[list[int]], r:int, c:int, k:int) -> bool:
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


def solve(sudoku: list[list[int]], r:int=0, c:int=0) -> bool:
    return False
    


if __name__ == "__main__":
    sudoku = create_sudoku_grid()
    print_sudoku_grid(sudoku)
