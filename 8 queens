def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_8_queens(board, row):
    # If all queens are placed, return the solution
    if row == 8:
        return [board[:]]  # Return a copy of the board

    solutions = []
    # Try placing queens in all columns for the current row
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            solutions += solve_8_queens(board, row + 1)  # Recursively place queens in the next row
            board[row] = -1  # Backtrack (remove the queen)
    return solutions

def print_solution(board):
    for row in board:
        for i in range(8):
            if(i==row):line='Q'
            else:line='.'
        #line = ['Q' if i == row else '.' for i in range(8)]  # Represent the board with 'Q' for queens
            print(" ".join(line))
    print()

def main():
    board = [-1] * 8  # Initialize an empty board with -1 (no queen placed)
    solutions = solve_8_queens(board, 0)
    
    print(f"Found {len(solutions)} solutions:")
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()
