import csv

def filter_csv1(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        games = []  # List to store individual games
        current_game = []  # List to store data for the current game

        # Iterate through each row in the CSV file
        for row in reader:
            if row[0] == 'A':  # If it's a row indicating a win for the AI
                if current_game:
                    # Convert string elements to float/int in the current game data
                    current_game = [[float(cell) for cell in game_row] for game_row in current_game]
                games.append(current_game)  # Add the completed game to the list of games
                current_game = []  # Reset current_game to start a new game
            elif row[0].isdigit() or row[0] == "-1":  # If the row starts with a digit (negative int aren't counted as digits) or -1
                current_game.append(row)  # Add the row to the current game data
            elif row[0] == 'P' or row[0] == 'D':  # If it's a row indicating a win for the Player or draw
                current_game.append(row)  # Add the row to the current game data
                current_game = []  # End the current game

    # Write the filtered data to the output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for game in games:
            for row in game:
                writer.writerow(row)

# Call the function to filter game data and save it to output files
filter_csv1("game_data.txt", "output.txt")  # Filter game data
filter_csv1("zug_data.txt", "zug_output.txt")  # Filter move data