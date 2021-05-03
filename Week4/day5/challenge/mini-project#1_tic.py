# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across,
# or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks 
# in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more 
# helper functions or choose a completely different appoach if you want.

# Tips : Consider The Following:
# What functionality will need to occur every turn to make this program work?
# After contemplating the question above, think about splitting your code into 
# smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

#Board
#display board
#play game
#handle turn 
# check win
    #check rows 
    #check columns 
    #check diagonals
#check tie 
#change between each player


board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

def display_board():
    print('*************')
    print(f'* + {board[0][1]} +  |  + {board[0][1]} +  |  + {board[0][2]} + *')
    print(f'* + {board[1][0]} +  |  + {board[1][1]} +  |  + {board[1][2]} + *')
    print(f'* + {board[2][0]} +  |  + {board[2][1]} +  |  + {board[2][2]} + *')
    print('*************')
    
display_board()

plr_x= []

turns_x = 0
turns_o= 0
 
def player_input(turns_x = 0, turns_o = 0):
        total_turns = turns_x + turns_y
        if total_turns is > 9: 
            print('game over, do u want to play agin?')         
        if turns_x == turns_y:
            print('Player X turn')
            x_row = input('select Row ')
            x_col = input('select Col ')
            turns_x +=1
        else:
            print('Player O turn')
            o_row = input('select Row ')
            o_col = input('select Col ')
            turns_o +=1
                    
        # for x in board:
        #     board[x_row][x_col] = X
        

        



player_input()

board[x_row][x_col]