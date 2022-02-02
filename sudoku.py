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
    

sudoku_print(sudoku_test)