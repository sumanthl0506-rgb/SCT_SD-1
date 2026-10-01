def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    if num in board[row]:
        return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i!= 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example unsolved puzzle - SkillCraft will test with this
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("--- Task 03: Sudoku Solver | SkillCraft Technology ---")
print("Unsolved Board:")
print_board(board)
print("\nSolving...\n")

solve_sudoku(board)

print("Solved Board:")
print_board(board)
