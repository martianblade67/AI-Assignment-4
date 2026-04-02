board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return (i, j)
    return None

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    box_row, box_col = 3*(row//3), 3*(col//3)
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            if board[i][j] == num:
                return False
    
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    
    for num in "123456789":
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve(board):
                return True
            
            board[row][col] = '.'
    
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            print(board[i][j], end=" ")
        
        print()

solve(board)
print_board(board)