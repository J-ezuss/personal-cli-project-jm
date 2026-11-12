def get_move(player_name):
    while True:
        move = input(player_name + ", choose rock, paper or scissors: ")
        move = move.lower().strip()
        if move == "rock" or move == "paper" or move == "scissors":
            return move
        print("That is not a move. Try again.")


def get_winner(move1, move2):
    if move1 == move2:
        return 0
    elif move1 == "rock" and move2 == "scissors":
        return 1
    elif move1 == "paper" and move2 == "rock":
        return 1
    elif move1 == "scissors" and move2 == "paper":
        return 1
    else:
        return 2
