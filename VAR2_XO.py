def rules():
    print("""
Перед вами игра "крестики-нолики".
Игроки по очереди ставят данные символы на свободные клетки поля 3×3. 
Победителем считается тот, кто первым выстроит непрерывный ряд
из крестиков или ноликов в любом направлении: по вертикали, горизонтали, диагонали.
Цифры на полях указывают на ячейку, куда нужно ставить символ.
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
""")


def start(question):  # функция задающая вопрос
    answer = None  # ответ
    while answer not in ("да", "нет"):  # "Крестики начинают игру, хотите сделать ход первым?"
        answer = input(question).lower()
    return answer


def symbol():  # присвоение игроку символа (x, o)
    start_1 = start("Крестики начинают игру, хотите сделать ход первым?")
    if start_1 == "да":
        print("Отлично, Вы играете крестиками!")
        player_1 = O
        player_nas = X
    else:
        print("Хорошо, мой ход первый")
        player_1 = X
        player_nas = O
    return player_1, player_nas


X = "X"  # глобально задаем переменные
O = "O"


def step_number(low, high):  # выбор свободной ячейки, куда игрок хочет поставить свой символ
    answer = None
    while answer not in range(low, high):  # пока нужного ответа нет в пределах 0-8, вывод вопроса
        answer = int(input("Делайте свой ход, выберите свободную ячейку от 0-8: "))
    return answer


SIZE_BOARD = 9  # размер доски
STEP = ' '  # доступная пустая ячейка


def new_board():  # функция, создающая каждый раз новую доску
    board = []
    for i in range(SIZE_BOARD):
        board.append(STEP)
    return board


def show_new_board(board):  # функция, которая показывает доску с результатом каждого хода
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------'),
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')


def available_step(board):  # функция доступности шагов
    available_step = []
    for i in range(SIZE_BOARD):
        if board[i] == STEP:
            available_step.append(i)
    return available_step


NOBODY_WIN = 'Ничья!!!'


def king(board):  # функция, выводит победителя (victory варианты победных комбинаций)

    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]] != STEP:
            king = board[i[0]]
            return king
        if STEP not in board:
            return NOBODY_WIN
    return None      # игра еще не дошла до конца


def player_nas_step(board, player_nas):   # функция принимает доску и символ игрока (игрок делает ход)
    available = available_step(board)
    step = None
    while step not in available:
        step = step_number(0, SIZE_BOARD)
        if step not in available:
            print('Поле занято. Напиши другой номер: ')
    print('Ok!')
    return step


def player_1_step(board, player_1, player_nas):  # функция ходов компьютера

    print('Мой ход: ')
    for i in available_step(board):
        board[i] = player_1
        if king(board) == player_1:
            print(i)
            return i
        board[i] = STEP
    for j in available_step(board):
        board[j] = player_nas
        if king(board) == player_nas:
            print(j)
            return j
        board[j] = STEP
    for k in available_step(board):
        print(k)
        return k


def next_queue(queue):  # очередность ходов
    if queue == X:
        return O
    else:
        return X


def win_win(best_player, player_1, player_nas):  # функция для определения победителя
    if best_player != NOBODY_WIN:
        print('Собрана линия ', best_player)
    if best_player == player_1:
        print('!!!Компьютер выйграл!!!!')
    elif best_player == player_nas:
        print('!!!Победитель nas!!!')
    elif best_player == NOBODY_WIN:
        print(NOBODY_WIN)


def main():  # общая функция для вывода процесса игры
    rules()
    player_1, player_nas = symbol()
    queue = X
    board = new_board()
    show_new_board(board)
    while not king(board):
        if queue == player_nas:
            step = player_nas_step(board, player_nas)
            board[step] = player_nas
        else:
            step = player_1_step(board, player_1, player_nas)
            board[step] = player_1
        show_new_board(board)
        queue = next_queue(queue)
    best_player = king(board)
    win_win(best_player, player_1, player_nas)

main()
