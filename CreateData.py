# ---- IMPORT ----
import csv
import random

# ---- AI Move Function ----
def ai_move():
    """
    Generates a random move for the AI.
    Ensures that the move is legal (i.e., the cell is empty).
    """
    while True:
        move_ai = random.randint(0, 8)
        if board[move_ai] != 0:
            continue
        else:
            return move_ai

# ---- Game Win Function ----
def game_win():
    """
    Checks for a winning condition.
    Returns the player number (1 or -1) if there's a winner, otherwise returns False.
    """
    # Check rows
    if board[0] == board[1] == board[2]:
        return board[0]
    if board[3] == board[4] == board[5]:
        return board[3]
    if board[6] == board[7] == board[8]:
        return board[6]

    # Check columns
    if board[0] == board[3] == board[6]:
        return board[0]
    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]

    # Check diagonals
    if board[0] == board[4] == board[8]:
        return board[0]
    if board[2] == board[4] == board[6]:
        return board[2]
    else:
        return False

# ---- Game Draw Function ----
def game_draw():
    """
    Checks if the game is a draw.
    A draw occurs when all cells are filled and there's no winner.
    """
    check_draw = True
    for i in range(9):
        if board[i] == 0:
            check_draw = False
    if game_win() == False and check_draw == True:
        return True

# ---- Collect Data Function ----
def collect_data(file, data):
    """
    Appends the provided data to a CSV file.
    """
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# ---- MAIN ----
for i in range(1000):
    game_running = True
    board = [0 for _ in range(9)]  # Initialize the board with all cells set to 0

    while game_running:
        # AI 1 makes a move
        move_ai_1 = ai_move()
        collect_data('zug_data.txt', [move_ai_1])  # Record the move
        board[int(move_ai_1)] = 1  # AI 1 marks its move on the board
        collect_data('game_data.txt', board)  # Record the board state

        # Check for a win or draw
        win = game_win()
        if win == 1:
            collect_data('game_data.txt', ['P'])  # AI 1 wins
            collect_data('zug_data.txt', ['P'])
            game_running = False
            break
        draw = game_draw()
        if draw:
            collect_data('game_data.txt', ["D"])  # Draw
            collect_data('zug_data.txt', ['D'])
            game_running = False
            break

        # AI 2 makes a move
        move_ai_2 = ai_move()
        collect_data('zug_data.txt', [move_ai_2])  # Record the move
        board[int(move_ai_2)] = -1  # AI 2 marks its move on the board
        collect_data('game_data.txt', board)  # Record the board state

        # Check for a win or draw
        win = game_win()
        if win == -1:
            collect_data('game_data.txt', ["A"])  # AI 2 wins
            collect_data('zug_data.txt', ["A"])
            game_running = False
            break
        draw = game_draw()
        if draw:
            collect_data('game_data.txt', ["D"])  # Draw
            collect_data('zug_data.txt', ["D"])
            game_running = False
            break
