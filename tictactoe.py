#global variable


board=["-","-","-","-","-","-","-","-","-"]
game_is_on=True
winner=None
current_player="X"

#display board
def display_sample():
    print("THE IS SAMPLE BOARD \n\n")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")
    print("\n")
    
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
    
display_sample()

        
def play_game():
    
    #display inital board
    display_board()
    print("\n")

    
    #while game is still is going
    while game_is_on:
        handle_turn(current_player)
        
        check_if_game_is_over()
        # flip to the other player
        flip_player()
        
        
    #print the winner 
    if winner == "X" or winner =="O":
        print(winner + " Won the game .")
    elif winner == None:
        print("\nThe Game is  Tie .")

            
#hande a turn 
def handle_turn(player):
    print(player + "'s turn.")
    position=input("Choose a positon from 1-9:  ")
    valid =False
    while not valid:
    
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("\n Please Choose a positon from 1-9:  ")


        position=int(position)-1
        if board[position] == "-":
            valid =True
        else:
            print(" \n Please choose another")

    
    board[position]=player
    display_board()

    
    
def check_if_game_is_over():
    check_for_winner()
    check_if_tie()

    
    
def check_for_winner():
    #to access global variable we have to decleare it in function
    global winner
    #check rows
    row_winner=check_rows()
    #check column
    column_winner=check_column()
    #check diagonal
    diagonal_winner=check_diagonal()
    
    if row_winner:
        winner=row_winner
        
    elif column_winner:
        winner=column_winner
        
    elif diagonal_winner:
        winner=diagonal_winner
        
    else:
        #no winner
        winner=None
    

    
def check_rows():
    global game_is_on
    row_1=board[0] == board[1] == board[2] != "-"
    row_2=board[3] == board[4] == board[5] != "-"
    row_3=board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_on = False
    #return the winner i.e.  X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    
    
def check_column():
    global game_is_on
    column_1=board[0] == board[3] == board[6] != "-"
    column_2=board[1] == board[4] == board[7] != "-"
    column_3=board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_is_on = False
    #return the winner i.e.  X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2] 

    
    
def check_diagonal():
    global game_is_on
    diagonal_1=board[0] == board[4] == board[8] != "-"
    diagonal_2=board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2 :
        game_is_on = False
    #return the winner i.e.  X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]


    
def check_if_tie():
    global game_is_on
    if "-" not in board:
        game_is_on =False
    return



#change the player 
def flip_player():
    global current_player
    if current_player == "X":
        current_player ="O"
        
    
    elif current_player == "O":
        current_player ="X"
           
    
    
play_game()