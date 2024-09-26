def print_board(board):
    for row in board:
        print(' '.join('Q' if cell else '.' for cell in row))
    print()
def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False
    return True
def solve_n_queens(board, row):
    if row >= len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = False
    return False
def solve_8_queens():
    board = [[False] * 8 for _ in range(8)]
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists")
# Example usage
solve_8_queens()