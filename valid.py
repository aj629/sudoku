import solver

def construct_board():
    """
    Constructs a valid sudoku board based on a .txt file or user inputs each row

    Each line in the text file has to be integers and commas with no spaces.
    Each line would represent a row on the board and

    For user inputs, each row would also be integers and commas and no spaces
    """
    
    text_or_constr = input(
        """Would you like to construct your own board or input a .txt file? Please type 
        the word Construct or the word File
        """)
    text_or_constr = text_or_constr.title()

    # if a file was inputted, read the file for the rows of a board
    if text_or_constr == 'File':
        file_name = input("Please type the file path to the .txt file: ")
        try:
            file1 = open(file_name, 'r')
            lines = file1.readlines()
        except FileNotFoundError:
            print(f"Invalid file name!: {file_name}")
            return
        except NotADirectoryError:
            print(f"Not a directory {file_name}")
            return

        # loop over each line and add it to the board after converting to list
        for line in lines:
            list_frag = list_constr(line)
            board.append(list_frag)



    #if user is constructing their own board
    elif text_or_constr == 'Construct':
        length = int(input("How many rows does your board have? Please enter as an integer such as 9: "))

        #loop over that many rows as given by user
        for i in range(length):
            list_frag = list_constr(i)
            # makes sure that the rows are same length, if they are then add them to board
            if len(board) != 0 and len(list_frag) != len(board[0]):
                print("Invalid row length. Rows must be the same length")
            else:
                board.append(list_frag)
    else:
        print("Invalid answer please try again! \n")
        construct_board()
    
def list_constr(frag):
    """
    Reads line from a file and add returns it as type list.
    OR asks for user to input a specific row and return it as type list

    Parameter frag: must be type int or type str
    """
    if type(frag) is int:
        fragment = input(f"Row {input}: ")
        try:
            list_frag = [int(x) for x in fragment.split(',')]
        except ValueError:
            print("Invalid row format, please try again")
            list_frag = list_constr(frag)
    elif type(frag) is str:
        fragment = frag  
        list_frag = [int(x) for x in fragment.split(',')]

    return list_frag


def valid(board):
    """
    Return True if each box, each row, and each column of the board is valid
    according to sudoku rules.

    Parameter board: 2D list of ints
    """

    # checks every row
    row_valid = True
    for i in range(len(board)):
        checking = check_row(board,i)
        row_valid = row_valid and checking

    # checks every column
    col_valid = True
    for i in range(len(board)):
        checking = check_column(board,i)
        col_valid = col_valid and checking

    # checks every box
    box_valid = True
    for i in range(box_size):
        for j in range(box_size):
            checking = check_box(board, i, j, box_size)
            box_valid = box_valid and checking

    # all three must be true for a valid board
    final = row_valid and box_valid and col_valid
    print(row_valid)
    print(box_valid)
    print(col_valid)

    return final
    

def solve_valid(board):
    """
    If the board is valid, solve the board is the user inputs the string Yes
    
    Parameter board: 2D list of ints
    """

    #check if board is valid
    validility = valid(board)

    # loop variable for while loop
    answering = True

    if validility:
        while answering:
            print("The board is valid!!!")

            #ask for user input
            solve = input("Would you like to solve this sudoku board? Please enter Yes or No ")
            solve = solve.title()

            # different cases for Yes or No
            # if yes, solve the board. if no, end loop
            if solve == 'Yes':
                solver.solver(board, box_size)
                answering = False
            elif solve == 'No':
                print("Okay...bye :)")
                answering = False
            else:
                print("Invalid input please try again")
    else:
        print("The board is not valid. Please fix your board and try again")


def check_row(board,row):
    """
    Returns True if that particular row of the board is valid according to sudoku rules
    
    Parameter board: 2D list of ints
    Parameter row: the row of the board that is being check, type int
    """

    # a set to keep track of all the numbers you have seen
    checked = set()

    # loops over the length of a row and checks every num in that row
    for i in range(len(board[0])):
        num = board[row][i]

        # if the number already the set then the row violates the rules
        if num in checked:
            return False

        # if the number is not within valid range then return False
        elif num < 0 or num > len(board):
            return False
        # if the position is not empty but in range then add it to the set.
        elif num >= 1 and num <= len(board):
            checked.add(num)
    return True

def check_column(board, column):
    """
    Returns True if that particular col of the board is valid according to sudoku rules
    
    Parameter board: 2D list of ints
    Parameter col: the col of the board that is being check, type int
    """
    checked = set()
    for i in range(len(board)):
        num = board[i][column]

       # if the number already the set then the col violates the rules
        if num in checked:
            return False

        # if the number is not within valid range then return False
        elif num < 0 or num > len(board):
            return False
        # if the position is not empty but in range then add it to the set.
        elif num >= 1 and num <= len(board):
            checked.add(num)
    return True

def check_box(board, row, col, box_size):
    """
    Returns True if that particular box that contains the position (row,col) is 
    valid according to sudoku rules.
    
    Parameter board: 2D list of ints
    Parameter row: the row of the board that is being check, type int
    Parameter col: the col of the board that is being check, type int
    Parameter box_size: is the smaller grid size of the board. 
    EX: traditional boards have nine 3 by 3 boxes so box_size would be the int 3
    
    """
    # maintains the number that were already observed
    checked = set()

    # loops over the particular box that (row,col) is in
    # we multliply by box_size to get the correct starting indices.
    # our loop will go box_size times as that is the length the cube
    print()
    for i in range(row * box_size, row * box_size + box_size):
        # an inner loop of the same length is necessary as each row of the cube needs to be checked as well
        for j in range(col * box_size, col * box_size + box_size):
            num = board[i][j]
            print(f"this is num for box {num}")
        # if the number already the set then the col violates the rules
            if num in checked:
                print(f"this num already exist: {num}. we aree at {row},{col}")
                return False

            # if the number is not within valid range then return False
            elif num < 0 or num > len(board):
                print(f"this number violates: {num}")
                return False
            # if the position is not empty but in range then add it to the set.
            elif num >= 1 and num <= len(board):
                print(f"this num DNE so im adding: {num}")
                checked.add(num)
    return True



print("""Please enter a valid Sudoku board in following form with zeroes
representing empty space:
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7] \n""")

print("""Note: The Brackets are there to make visualization easy. Your input for 
    each row should just be integers seperate by commas. For example, the first row in
    the board above would be inputted as 7,8,0,4,0,0,1,2,0
    If you do, please enter one row at a time.

    Or alternatively you can provide a .txt where each line would be a row of the board.
    """)

# an empty list to reconstruct the board based on user input
board = []

# call to construct board
construct_board()
print(f"This si lenght of board: {len(board)}")


box_size = input("""
    Please input the box size of your sudoku board. For example, traditional boards 
    have nine 3 X 3 boxes with digits from 1 to 9. Your input would be the integer 3 
    """) 

box_size = int(box_size)
# call to solve board if desired
solve_valid(board)
