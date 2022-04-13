# board/ all pieces
# show board
# handle turn
# switch player
# play game

limit = ['0', '1', '2', '3', "4", '5', '6', '7']

board = [['-']*8 for i in range(8)]

board[0][0] = 'x'
board[0][2] = 'x'
board[0][4] = 'x'
board[0][6] = 'x'
board[1][1] = 'x'
board[1][3] = 'x'
board[1][5] = 'x'
board[1][7] = 'x'
board[2][0] = 'x'
board[2][2] = 'x'
board[2][4] = 'x'
board[2][6] = 'x'

board[7][1] = 'o'
board[7][3] = 'o'
board[7][5] = 'o'
board[7][7] = 'o'
board[6][0] = 'o'
board[6][2] = 'o'
board[6][4] = 'o'
board[6][6] = 'o'
board[5][1] = 'o'
board[5][3] = 'o'
board[5][5] = 'o'
board[5][7] = 'o'

game_still_on = True          
current_player = 'x'
point_x = 0
point_o = 0

def showboard():
    
    print(f"\n       0    1    2    3    4    5    6    7\n")
    print(f"7    {board[7]}    7")
    print(f"6    {board[6]}    6")
    print(f"5    {board[5]}    5")
    print(f"4    {board[4]}    4")
    print(f"3    {board[3]}    3")
    print(f"2    {board[2]}    2")
    print(f"1    {board[1]}    1")
    print(f"0    {board[0]}    0")
    print(f"\n       0    1    2    3    4    5    6    7\n")

def game_start():

    while game_still_on:

        pick_piece()

def pick_piece():

    global point
    global current_player

    print(f"Its {current_player}'s Turn!")
    coord1 = input("Choose your piece[x,y]: ")

    if len(coord1) != 3:
        print("Invalid move")
        coord1 = ''
        pick_piece()
        
    old = coord1.split(",")
    if len(old) != 2:
        print("Invalid move")
        pick_piece()
    
    elif old[0] not in limit and old[1] not in limit:
        print("Invalid move")
        pick_piece()
    else:
        old_x = int(old[0])
        old_y = int(old[1])

        if board[old_y][old_x] == 'X':
            current_player = 'X'
        elif board[old_y][old_x] == 'O':
            current_player = 'O'
        if board[old_y][old_x] == current_player:
            move_to(old_y, old_x)
        else:
            print("Invalid move")
            pick_piece()

def move_to(y, x):

    global new_y
    global new_x
    global current_player
    global game_still_on

    coord2 = input("Choose your move[x,y]: ")

    if len(coord2) != 3:
        print("Invalid move")
        reset()
        coord2 = ''
        pick_piece()

    new = coord2.split(",")
    if len(new) != 2:
        print("Invalid move")
        reset()
        pick_piece()

    elif new[0] not in limit and new[1] not in limit:
        print("Invalid move")
        reset()
        pick_piece()
    else:
        new_x = int(new[0])
        new_y = int(new[1])
        
        available_move(y, x)
        showboard()
        check_win()
        reset()
        flip_player()
        print(f"Capture: x: {point_x} | o: {point_o}")

def available_move(oldY, oldX):

    global new_y
    global new_x
    global point_x
    global point_o

# 1 place movement

    if  board[new_y][new_x] == '-' and new_y == (oldY + 1) and new_x == (oldX + 1) and current_player == 'x': 

        #for 'x' 1 place movement [UP RIGHT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY + 1) and new_x == (oldX - 1) and current_player == 'x':

        #for 'x' 1 place movement [UP LEFT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY - 1) and new_x == (oldX + 1) and current_player == 'o':

        #for 'o' 1 place movement [DOWN RIGHT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY - 1) and new_x == (oldX - 1) and current_player == 'o':

        #for 'o' 1 place movement [DOWN LEFT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

# 2 place movement [capture]

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX + 2) and board[oldY + 1][oldX + 1] != current_player and board[oldY + 1][oldX + 1] != '-' and current_player == 'x':

        #for 'x' 2 place movement [UP RIGHT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX + 1] = '-'
        point_x += 1
 
        if new_y != 6 and new_y != 7:
            if new_x != 6 and new_x != 7:
                if (board[new_y + 2][new_x + 2] == '-' and board[new_y + 1][new_x + 1] == 'o'):

                    #for 'x' jumping [UP RIGHT] [CAPTURE]

                    reset()
                    flip_player()

            if new_x != 0 and new_x != 1:
                if board[new_y + 2][new_x - 2] == '-' and board[new_y + 1][new_x - 1] == 'o':

                    #for 'x' jumping [UP LEFT] [CAPTURE]

                    reset()
                    flip_player()

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX - 2) and board[oldY + 1][oldX - 1] != current_player and board[oldY + 1][oldX - 1] != '-' and current_player == 'x':

        #for 'x' 2 place movement [UP LEFT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX - 1] = '-'
        point_x += 1

        if new_y != 6 and new_y != 7:
            if new_x != 6 and new_x != 7:
                if board[new_y + 2][new_x + 2] == '-' and board[new_y + 1][new_x + 1] == 'o':

                    #for 'x' jumping [UP RIGHT] [CAPTURE]

                    reset()
                    flip_player()
            
            if new_x != 0 and new_x != 1:
                if board[new_y + 2][new_x - 2] == '-' and board[new_y + 1][new_x - 1] == 'o':

                    #for 'x' jumping [UP LEFT] [CAPTURE]

                    reset()
                    flip_player()

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX + 2) and board[oldY - 1][oldX + 1] != current_player and board[oldY - 1][oldX + 1] != '-' and current_player == 'o':

        #for 'o' 2 place movement [DOWN RIGHT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX + 1] = '-'
        point_o += 1

        if new_y != 0 and new_y != 1:
            if new_x != 6 and new_x != 7:
                if board[new_y - 2][new_x - 2] == '-' and board[new_y - 1][new_x - 1] == 'x':

                    #for 'o' jumping  [DOWN LEFT] [CAPTURE]

                    reset()
                    flip_player()

                if board[new_y - 2][new_x + 2] == '-' and board[new_y - 1][new_x + 1] == 'x':

                    #for 'o' jumping [DOWN RIGHT] [CAPTURE]

                    reset()
                    flip_player()            

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX - 2) and board[oldY - 1][oldX - 1] != current_player and board[oldY - 1][oldX - 1] != '-' and current_player == 'o':

        #for 'o' 2 place movement [DOWN LEFT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX - 1] = '-'
        point_o += 1

        if new_y != 0 and new_y != 1:
            if new_x != 0 and new_x != 1:
                if board[new_y - 2][new_x - 2] == '-' and board[new_y - 1][new_x - 1] == 'x':

                    #for 'o' jumping  [DOWN LEFT] [CAPTURE]

                    reset()
                    flip_player()

            if new_x != 6 and new_x != 7:
                if board[new_y - 2][new_x + 2] == '-' and board[new_y - 1][new_x + 1] == 'x':

                    #for 'o' jumping [DOWN RIGHT] [CAPTURE]

                    reset()
                    flip_player()       

# 1 place movemnt KING

    elif board[new_y][new_x] == '-' and new_y == (oldY + 1) and new_x == (oldX + 1) and ( current_player == "X" or current_player == 'O' ):

        #for KING 1 place movement [UP RIGHT] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY + 1) and new_x == (oldX - 1) and ( current_player == "X" or current_player == 'O' ):

        #for KING 1 place movement [UP LEFT] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY - 1) and new_x == (oldX + 1) and ( current_player == "X" or current_player == 'O' ):

         #for KING 1 place movement [DOWN RIGHT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

    elif board[new_y][new_x] == '-' and new_y == (oldY - 1) and new_x == (oldX - 1) and ( current_player == "X" or current_player == 'O' ):

        #for KING 1 place movement [DOWN LEFT]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player

# 2 place movement KING "X" capture {WORK FROM HEREEEE}

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX + 2) and board[oldY + 1][oldX + 1] != current_player and board[oldY + 1][oldX + 1] != '-' and current_player == 'X':

        #for KING 'x' 2 place movement [UP RIGHT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX + 1] = '-'
        point_x += 1

        jumpingX(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX - 2) and board[oldY + 1][oldX - 1] != current_player and board[oldY + 1][oldX - 1] != '-' and current_player == 'X':

        #for KING 'x' 2 place movement [UP LEFT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX - 1] = '-'
        point_x += 1

        jumpingX(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX + 2) and board[oldY - 1][oldX + 1] != current_player and board[oldY - 1][oldX + 1] != '-' and current_player == 'X':

        #for KING 'x' 2 place movement [DOWN RIGHT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX + 1] = '-'
        point_x += 1

        jumpingX(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX - 2) and board[oldY - 1][oldX - 1] != current_player and board[oldY - 1][oldX - 1] != '-' and current_player == 'X':

        #for KING 'x' 2 place movement [DOWN LEFT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX - 1] = '-'
        point_x += 1

        jumpingX(new_x, new_y)

# 2 place movemetn KING "O" capture

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX + 2) and board[oldY + 1][oldX + 1] != current_player and board[oldY + 1][oldX + 1] != '-' and current_player == 'O':

        #for KING 'o' 2 place movement [UP RIGHT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX + 1] = '-'
        point_o += 1

        jumpingO(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY + 2) and new_x == (oldX - 2) and board[oldY + 1][oldX - 1] != current_player and board[oldY + 1][oldX - 1] != '-' and current_player == 'O':

        #for KING 'o' 2 place movement [UP LEFT] [capture] 

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY + 1][oldX - 1] = '-'
        point_o += 1

        jumpingO(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX + 2) and board[oldY - 1][oldX + 1] != current_player and board[oldY - 1][oldX + 1] != '-' and current_player == 'O':

        #for KING 'o' 2 place movement [DOWN RIGHT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX + 1] = '-'
        point_o += 1

        jumpingO(new_x, new_y)

    elif board[new_y][new_x] == '-' and new_y == (oldY - 2) and new_x == (oldX - 2) and board[oldY - 1][oldX - 1] != current_player and board[oldY - 1][oldX - 1] != '-' and current_player == 'O':

        #for KING 'o' 2 place movement [DOWN LEFT] [capture]

        board[oldY][oldX] = '-'
        board[new_y][new_x] = current_player
        board[oldY - 1][oldX - 1] = '-'
        point_o += 1

        jumpingO(new_x, new_y)

    else:
        print("Invalid move")
        reset()
        pick_piece()

    check_king()

    return point_x, point_o

def flip_player():

    global current_player

    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"

    return current_player

def check_king():

    global current_player

    if 'x' in board[7]:
        board[new_y][new_x] = 'X'

    if 'o' in board[0]:
        board[new_y][new_x] = 'O'
    
def reset():

    global current_player

    if current_player == 'X':
        current_player = 'x'
    elif current_player == 'O':
        current_player = 'o'

def check_win():

    global game_still_on
    xCount = 0
    oCount = 0

    # Check win for X
    for j in range(8):
        for i in board[j]:
            if i == 'x' or i == 'X':
                xCount += 1
    if xCount == 0:
        print("O Wins!")
        game_still_on = False

    # Check win for O
    for k in range(8):
        for l in board[k]:
            if l == 'o' or l == 'O':
                oCount += 1
    if oCount == 0:
        print("X Wins!")
        game_still_on = False

    return game_still_on

def jumpingX(new_x, new_y):

    if new_y != 6 and new_y != 7:
        if new_x != 6 and new_x != 7:
            if board[new_y + 2][new_x + 2] == '-' and board[new_y + 1][new_x + 1] == 'o':

                #for 'x' jumping [UP RIGHT] [CAPTURE]

                reset()
                flip_player()

        if new_x != 0 and new_x != 1:
            if board[new_y + 2][new_x - 2] == '-' and board[new_y + 1][new_x - 1] == 'o':

                #for 'x' jumping [UP LEFT] [CAPTURE]

                reset()
                flip_player()

    if new_y != 0 and new_y != 1:
        if new_x != 6 and new_x != 7:
            if board[new_y - 2][new_x + 2] == '-' and board[new_y - 1][new_x + 1] == 'o':

                    #for 'x' jumping [DOWN RIGHT] [CAPTURE]

                    reset()
                    flip_player()

        if new_x != 0 and new_x != 1:
            if board[new_y - 2][new_x - 2] == '-' and board[new_y - 1][new_x - 1] == 'o':

                #for 'x' jumping [DOWN LEFT] [CAPTURE]

                reset()
                flip_player()

def jumpingO(new_x, new_y):

    if new_y != 6 and new_y != 7:
        if new_x != 6 and new_x != 7:
            if board[new_y + 2][new_x + 2] == '-' and board[new_y + 1][new_x + 1] == 'x':

                #for 'o' jumping [UP RIGHT] [CAPTURE]

                reset()
                flip_player()

        if new_x != 0 and new_x != 1:
            if board[new_y + 2][new_x - 2] == '-' and board[new_y + 1][new_x - 1] == 'x':

                #for 'o' jumping [UP LEFT] [CAPTURE]

                reset()
                flip_player()

    if new_y != 0 and new_y != 1:
        if new_x != 6 and new_x != 7:
            if board[new_y - 2][new_x + 2] == '-' and board[new_y - 1][new_x + 1] == 'x':

                    #for 'o' jumping [DOWN RIGHT] [CAPTURE]

                    reset()
                    flip_player()

        if new_x != 0 and new_x != 1:
            if board[new_y - 2][new_x - 2] == '-' and board[new_y - 1][new_x - 1] == 'x':

                #for 'o' jumping [DOWN LEFT] [CAPTURE]

                reset()
                flip_player() 

showboard()
game_start()

#  ~ Now to start working on Player 2 (o) Its done! Good Job
#  ~ Check the win again...2 O's can be there too u know
#  ~ Now Finish it off with the check_if_win and we're done (i hope)

#  ~ You're Doing Great BTW! Keep Going!!
