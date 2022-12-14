# Создайте программу для игры в ""Крестики-нолики"".

X = "X"
O = "O"
empty = ' '
draw = "Ничья"
number_of_squares = 9


def display_instruct():
    print(
        """
Игра 'крестики-нолики'
Чтобы сделать свой ход, введите от 0 до 8
Числа соответсвуют полям доски:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
"""
    )


def ask_yes_no(question):
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    go_first = ask_yes_no("Хотите сделать первый ход? (да/нет): ")
    if go_first == "да":
        print("\n Вы играете крестиками!")
        human = X
        computer = O
    else:
        print("\n Компьютер ходит первым!")
        computer = X
        human = O
    return computer, human

def new_board():
    board = []
    for square in range(number_of_squares):
        board.append(empty)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t",  "---------")
    print("\n\t", board[3], "|", board[4],  "|", board[5])
    print("\t",  "---------")
    print("\n\t", board[6], "|", board[7],  "|",  board[8], "\n")


def legal_moves(board):
    moves = []
    for square in range(number_of_squares):
        if board[square] == empty:
            moves.append(square)
    return moves


def winner(board):
    victory_options = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))
    for row in victory_options:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
        if empty not in board:
            return draw
    return None


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number(
            "Выберите одно из полей (0-8):", 0, number_of_squares)
        if move not in legal:
            print("\nЭто поле уже занято. Выберите другое.\n")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print("Я выберу номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = empty
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def neXt_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    "Вы одержали победу!"
    if the_winner != draw:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил компьютер!")
    elif the_winner == human:
        print("Поздравляю, Вы победили!")
    elif the_winner == draw:
        print("Ничья!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = neXt_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
input("\n\nНажмите Enter, чтобы выйти.")
