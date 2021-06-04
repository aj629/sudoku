
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def solver(bo, box_size):
    """
    Solves a soduku board with backtracking and pretty prints the solved board

    Parameter bo: 2D list of ints
    Parameter box_size: is the smaller grid size of the board. 
    EX: traditional boards have nine 3 by 3 boxes so box_size would be the int 3
    """
    solve(bo, box_size)
    print_board(bo, box_size)

def solve(bo, box_size):
    """
    Solves a sodoku board with backtracking

    Parameter bo: 2D list of ints
    Parameter box_size: is the smaller grid size of the board. 
    EX: traditional boards have nine 3 by 3 boxes so box_size would be the int 3
    """


    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    # trys out numbers 1 through 25 inclusive for each position on the board
    # checks if the num is valid based on current board
    # recursively solves next positions
    # if no numbers work, then the position is reset to zero
    for i in range(1, len(bo)+1):
        if valid(bo, i, (row,col), box_size):
            bo[row][col] = i

            if solve(bo,box_size):
                return True
            
            bo[row][col] = 0 # resets the value.
    return False

def valid(bo, num, pos, box_size):
    """
    Returns True if num is valid at the pos position in the the 2D array
    
    Parameter bo: 2D list of ints
    Parameter num: the integer we are trying to insert at pos
    Parameter pos: (row, col)
    Parameter box_size: is the smaller grid size of the board. 
    EX: traditional boards have nine 3 by 3 boxes so box_size would be the int 3
    
    """

    # check row
    for i in range(len(bo[0])):
        # accesses a specific row and loop over all columns of that row
        # checks all columns of that row to see if that number is already present
        # we skip when pos[1] != i because we just inserted that number
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        # same logic as checking row but for column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # box_size by box_size cube
    # use int division here so you can can get which smaller cube you are in
    box_x = pos[1] // box_size
    box_y = pos[0] // box_size


    # loops over the particular box the pos parameter is in 
    # note the int division will always give us one the boxes by (box_x, box_y)
    # therefore we multliply by box_size to get the correct starting indices.
    # our loop will go box_size times as that is the length the cube
    
    for i in range(box_y * box_size, box_y * box_size + box_size):
        # an inner loop of the same length is necessary as each row of the cube needs to be checked as well
        for j in range(box_x * box_size, box_x * box_size + box_size):
            # checks all space in the cube to make sure the number doesn't already exist
            # also skips the current position we inserted 
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def print_board(bo, box_size):
    """
    Pretty print of a board

    Parameter bo: 2D list of ints
    Parameter box_size: is the smaller grid size of the board. 
    EX: traditional boards have nine 3 by 3 boxes so box_size would be the int 3
    """

    for i in range(len(bo)):
        if i % box_size == 0 and i != 0:
            print("- - - - " * box_size)
    
        for j in range(len(bo[0])):
            if j % box_size == 0 and j != 0:
                print(" | ", end= "")

            if j == len(bo[0]) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    Return (int,int) in the form of (row, col) of the position of zeroes on the board
    Parameter bo: 2D list of ints. Usually a partially completed board

    """
    # loops through the entire board and checks if a position on the board is a zero
    # use length(bo) since the board is a large square
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i,j) # row, col
    return None




## testing board

# print_board(board, 3)
# solve(board,3)
# print("_____________________________")
# print_board(board,3)