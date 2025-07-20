#AI Based Tic - Tac - Toe

import math
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def is_winner(brd, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(brd[pos] == player for pos in line) for line in win_positions)

def is_draw(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

def minimax(brd, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    if is_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board()

    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in get_available_moves(board):
                    board[move] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except:
                print("Please enter a number from 1 to 9.")

        print_board()

        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_move = best_move()
        board[ai_move] = 'O'
        print("AI played:")
        print_board()

        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play()
