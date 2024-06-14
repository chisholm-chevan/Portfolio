"""sudoku = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
"""

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def is_valid_move(board, row, col, num):
    for i in range(3):
        if board[row][i] == num or board[i][col] == num:
            return False
    return True


def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True


def sudoku_game():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    print("Welcome to 3x3 Sudoku!")
    print("Enter row, column, and number (e.g., 1 2 3) to place your number on the board.")

    while not is_board_full(board):
        print_board(board)
        try:
            row, col, num = map(int, input("Enter row, column, and number (e.g., 1 2 3): ").split())
            row -= 1
            col -= 1
            if 0 <= row < 3 and 0 <= col < 3 and 1 <= num <= 3 and is_valid_move(board, row, col, num):
                board[row][col] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row, column, and number separated by spaces.")

    print("Congratulations! You solved the Sudoku puzzle!")
    print_board(board)

sudoku_game()
"""
sudoku = [0, 0, 0]
sudoku2 = [0, 0, 0]
sudoku3 = [0, 0, 0]

print("Welcome to my Sudoku Game")
print("Please note only values of 1,2,3 can be entered")


def board():
    print(f"1: [{sudoku[0]}] 2: [{sudoku[1]}] 3: [{sudoku[2]}]")
    print(f"4: [{sudoku2[0]}] 5: [{sudoku2[1]}] 6: [{sudoku2[2]}]")
    print(f"7: [{sudoku3[0]}] 8: [{sudoku3[1]}] 9: [{sudoku3[2]}]")


print("Please select the number as the location you will enter")
x = int(input(":"))
for x in range(0,10):
    match x:
        case x if x == 1:
            print("Please enter a number 1 to 3:")
            i = int(input())
            sudoku[0] = i
            print(board())
            """

print("".join(['ab','pq','rs']))