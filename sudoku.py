sudoku_test = [[3,5,4,1,7,8,9,6,2],
               [6,1,2,9,3,5,4,7,8],
               [7,8,9,4,2,6,3,1,5],
               [1,4,3,5,6,9,2,8,7],
               [8,7,5,3,4,2,1,9,6],
               [2,9,6,8,1,7,5,4,3],
               [4,6,1,7,5,3,8,2,9],
               [5,2,8,6,9,4,7,3,1],
               [9,3,7,2,8,1,6,5,4]]

def sudoku_print(sudoku_board):
    # Print the sudoku board given as parameter
    for i in range(9):
        for j in range(9):
            if j==3 or j==6:
                print(' ',end=' ')      # after the 3rd and 6th column add a space between elements
            print(sudoku_board[i][j], end=' ')
        if i==2 or i==5:                # after the 3rd and 6th row
            print()                     # add a new line
            for iter in range(9+2):     # add a space for every element + 2 more for the spaces created above
                print(' ', end=' ')
            print()                     # add a new line after the line full of spaces
        else: print()                   # newline after each row

def sudoku_is_valid(sudoku_board):
    # Returns True if the board given as parameter is a complete sudoku board
    for i in range(8):
        for j in range(8):
            # Every number must be between 1 and 9
            if sudoku_board[i][j]<1 or sudoku_board[i][j] > 9:
                return False
            # Every number must be different from the other ones below him
            for compare_i in range(i+1,9):
                if sudoku_board[i][j] == sudoku_board[compare_i][j]:
                    return False
            # Every number must be different from the other ones on his right
            for compare_j in range(j+1,9):
                if sudoku_board[i][j] == sudoku_board[i][compare_j]:
                    return False

    for first_i in range(0,9,3):
        for first_j in range(0,9,3):
            for i in range(first_i + 3):
                for j in range(first_j + 3):
                    for compare_i in range(i,first_i + 3):
                        for compare_j in range(j, first_j + 3):
                            if i == compare_i and j == compare_j:
                                pass
                            else:
                                if sudoku_board[compare_i][compare_j] == sudoku_board[i][j]:
                                    return False

    return True

#sudoku_print(sudoku_test)
if(sudoku_is_valid(sudoku_test)):
    print('This is a valid sudoku board!')
else:
    print('This board is not valid!')