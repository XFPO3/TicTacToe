#import
import numpy as np
from tensorflow.keras.models import load_model

game_running = True
board = ["" for i in range(10)]
for i in range(9):
        board[i+1] = i + 1

# Function to print the current state of the board
def board_print(board):
    print(str(board[1]) + "|" + str(board[2]) + "|" + str(board[3]))
    print(str(board[4]) + "|" + str(board[5]) + "|" + str(board[6]))
    print(str(board[7]) + "|" + str(board[8]) + "|" + str(board[9]))

# Function to handle player move
def player_move():
    global board
    while True:
        move_p = input("Player move: ")
        if len(move_p) != 1:
            print("Invalid input. Try again.")
            continue
        if not (move_p.isdigit() and 1 <= int(move_p) <= 9):
            print("Invalid input. Try again.")
            continue
        if board[int(move_p)] == "X" or board[int(move_p)] == "O":
            print("Field already occupied. Try again.")
            continue
        else:
            return int(move_p) - 1

# Function for AI move prediction
def ai_move(board):
    # Prepare the input data
    board_status = [-1 if feld == 'X' else 1 if feld == 'O' else 0 for feld in board[1:10]]
    input = np.array([board_status])

    # Predict the move with the model
    prediction = model.predict(input)
    # Choose the best move (index of the maximum value)
    move = np.argmax(prediction)
    for i in range(10):
        if board[move] == "X" or board[move] == "O":
            prediction[0][move] = -np.inf
            move = np.argmax(prediction)
    return move + 1  # Return the position (1-based)

# Load the trained model
model = load_model("ai_trained.keras")

# Function to check if there is a winner
def game_win():
    if board[1] == board[2] == board[3]:
        return board[1]
    if board[4] == board[5] == board[6]:
        return board[4]
    if board[7] == board[8] == board[9]:
        return board[6]

    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]
    if board[3] == board[6] == board[9]:
        return board[3]

    if board[1] == board[5] == board[9]:
        return board[1]
    if board[3] == board[5] == board[7]:
        return board[3]
    else:
        return False

# Function to check if the game is a draw
def game_draw():
    # For a draw, all fields must be occupied and game_win must not be true
    check_draw = True
    for i in range(1, 10):
        if board[i] != "X" and board[i] != "O":
            check_draw = False

    if game_win() == False and check_draw == True:
        return True

# Main game loop
while game_running:
    print()
    move_p = player_move() + 1
    board[move_p] = "X"
    board_print(board)
    win = game_win()
    if win == "X":
        print("You have won!")
        game_running = False
        break
    draw = game_draw()
    if draw == True:
        print("The game is a draw")
        game_running = False

    print()
    move_ai = ai_move(board)
    board[move_ai] = "O"
    board_print(board)
    win = game_win()
    if win == "O":
        print("The AI has defeated you!")
        game_running = False
        break
    draw = game_draw()
    if draw == True:
        print("The game is a draw")
        game_running = False
        break
    print("The AI has made a move")

print()
