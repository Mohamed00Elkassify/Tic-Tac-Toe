import random
import os

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    #This function prints the game board
    clear_screen() #Clear the screen before siplaying the board
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_marker():
    #Let the player choose the marker
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: choose your marker (X,O) : ').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

def place_marker(board, position, marker):
    board[position] = marker

def play_first():
    #Randomly select who plays first
    if random.randint(0,1) == 0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board, position):
    #Check if the position is empty
    return board[position] == ' '

def full_check(board):
    #Check if the board is full
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True

def check_win(board, marker):
    #Check if the player has won the game
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
            (board[4] ==  marker and board[5] == marker and board[6] == marker) or 
            (board[7] ==  marker and board[8] == marker and board[9] == marker) or
            (board[1] ==  marker and board[5] == marker and board[9] == marker) or
            (board[3] ==  marker and board[5] == marker and board[7] == marker) or
            (board[1] ==  marker and board[4] == marker and board[7] == marker) or
            (board[2] ==  marker and board[5] == marker and board[8] == marker) or
            (board[3] ==  marker and board[6] == marker and board[9] == marker))

def player_choice(board, player_name):
    #Let the player choose the position
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input(f'{player_name.title()}, choose your next position(1:9): '))
    return position

def computer_choice(board):
    #Let the computer choose the position
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = random.randint(1,9)
    return position



def main():
    #Here starts the game
    print('Welcome to Tic Tac Toe')

    #Get the players names
    player_1_name = input('Enter the name of player 1: ')
    game_mode = input('enter F to play with a friend or C to play with the computer : ').upper()
    if game_mode == 'F':
        player_2_name = input('Enter the name of player 2: ')
    elif game_mode == 'C':
        player_2_name = 'Computer'

    while True:
        the_board = [' '] * 10
        player_1_marker, player_2_marker = player_marker()
        turn = play_first()
        print(f'{player_1_name.title() if turn == "player 1" else player_2_name.title()} goes first.')
        game_on = True

        while game_on:
            if turn == 'player 1':
                #Player 1 turn
                display_board(the_board)
                position = player_choice(the_board,player_1_name)
                place_marker(the_board, position, player_1_marker)
                if check_win(the_board, player_1_marker):
                    display_board(the_board)
                    print(f'Congratulations! {player_1_name.title()} has won the game')
                    game_on = False
                else:
                    if full_check(the_board):
                        display_board(the_board)
                        print('The game is draw!')
                        break
                    else:
                        turn = 'player 2'

            else:
                #Player 2 turn
                display_board(the_board)
                if game_mode == 'F':
                    position = player_choice(the_board, player_2_name)
                elif game_mode == 'C':
                    position = computer_choice(the_board)
                place_marker(the_board, position, player_2_marker)
                if check_win(the_board, player_2_marker):
                    display_board(the_board)
                    print(f'Congratulations! {player_2_name.title()} has won the game')
                    game_on = False
                else:
                    if full_check(the_board):
                        display_board(the_board)
                        print('The game is draw!')
                        break
                    else:
                        turn = 'player 1'
        break
main()