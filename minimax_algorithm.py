
def best_move(game_board,i,turn):
    if game_board[i] == game_board[i + 1] and game_board[i] == game_board[1 + 2] and game_board[i] == turn:
        return turn
    elif game_board[i] == game_board[i + 4] and game_board[i] == game_board[1 + 8] and game_board[i] == turn:
        return turn
    elif game_board[i] == game_board[i + 3] and game_board[i] == game_board[1 + 6] and game_board[i] == turn:
        return turn
    elif game_board[i + 1] == game_board[i + 4] and game_board[i + 1] == game_board[1 + 7] and game_board[i + 1] == turn:
        return turn
    elif game_board[i + 2] == game_board[i + 4] and game_board[i + 2] == game_board[1 + 6] and game_board[i + 2] == turn:
        return turn
    elif game_board[i + 2] == game_board[i + 5] and game_board[i + 2] == game_board[1 + 8] and game_board[i + 2] == turn:
        return turn
    elif game_board[i + 3] == game_board[i + 4] and game_board[i + 3] == game_board[1 + 5] and game_board[i + 3] == turn:
        return turn
    elif game_board[i + 6] == game_board[i + 7] and game_board[i + 6] == game_board[1 + 8] and game_board[i + 6] == turn:
        return turn
    else:
        return false


    def tie(game_board):
        for i in range(len(game_board)):
            if game_board[i] != 'X' and game_board[i] != 'O':
                return false
            return true


def minimax(game_board, max):
    if best_moves(game_board, 0, 'X'):
        return 1
    elif best_move(game_board,0,'X'):
        return -1
    elif tie(game_board):
        return 0

    if max:
        best_outcome = -10
        for i in range(len(game_board)):
            if game_board[i] != 'X' and game_board[i] != 'O':
                game_board[i] = 'X'
                get_move = minimax(game_board, False)
                game_board[i] = i
                if get_move > best_outcome:
                    best_outcome = get_move
                    return best_outcome