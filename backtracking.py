from numpy import array

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def not_in_row(value, board, y):
    if value not in board[y]:
        return True
    else:
        return False


def not_in_col(value, board, x):
    col = []
    for row in range(9):
        col.append(board[row][x])
    if value not in col:
        return True
    else:
        return False


def not_in_3x3(value, board, coordinate):
    y = 3*(coordinate[0]//3)
    x = 3*(coordinate[1]//3)
    for j in range(3):
        for i in range(3):
            if value == board[y+j][x+i]:
                return False
    return True


def validate(solution):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True


def empty_cells(board):
    cells = []
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 0:
                cells.append([y, x])
    return cells


def backtrack(state):
    if len(empty_cells(state)) == 0:
        print("Solution:\n", array(state))
    for coordinate in empty_cells(state):
        for value in range(1, 10):
            if not_in_3x3(value, state, coordinate) and not_in_col(value, state, coordinate[1]) and not_in_row(value, state, coordinate[0]):
                state[coordinate[0]][coordinate[1]] = value
                backtrack(state)
        state[coordinate[0]][coordinate[1]] = 0
        return


backtrack(board)
