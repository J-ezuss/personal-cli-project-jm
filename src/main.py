import menu
import game

matches = []


def add_match(mode, player1, player2, move1, move2, winner):
    match = {
        "mode": mode,
        "player1": player1,
        "player2": player2,
        "move1": move1,
        "move2": move2,
        "winner": winner,
    }
    matches.append(match)


def show_result(player1, player2, move1, move2, winner):
    print(player1 + " chose " + move1)
    print(player2 + " chose " + move2)
    if winner == 0:
        print("It's a tie")
    elif winner == 1:
        print(player1 + " wins")
    else:
        print(player2 + " wins")


def show_matches():
    if len(matches) == 0:
        print("No matches yet.")
        return
    print("---- Match History ----")
    number = 1
    for match in matches:
        if match["winner"] == 0:
            result = "Tie"
        elif match["winner"] == 1:
            result = match["player1"] + " won"
        else:
            result = match["player2"] + " won"
        print(
            str(number)
            + ". "
            + match["player1"]
            + " ("
            + match["move1"]
            + ") vs "
            + match["player2"]
            + " ("
            + match["move2"]
            + ") - "
            + result
        )
        number = number + 1


def ask_match_number():
    show_matches()
    if len(matches) == 0:
        return -1
    number = input("Which match number? ")
    if not number.isdigit():
        print("Please type a number.")
        return -1
    number = int(number)
    if number < 1 or number > len(matches):
        print("There is no match with that number.")
        return -1
    return number - 1


def edit_match():
    index = ask_match_number()
    if index == -1:
        return
    match = matches[index]
    new_name1 = input(
        "New name for player 1 (Enter to keep " + match["player1"] + "): "
    )
    new_name2 = input(
        "New name for player 2 (Enter to keep " + match["player2"] + "): "
    )
    if new_name1 != "":
        match["player1"] = new_name1
    if new_name2 != "":
        match["player2"] = new_name2
    print("Match updated.")


def play_1v1():
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    move1 = game.get_move(player1)
    print("\n" * 40)
    move2 = game.get_move(player2)
    winner = game.get_winner(move1, move2)
    show_result(player1, player2, move1, move2, winner)
    add_match("1v1", player1, player2, move1, move2, winner)


def main():
    while True:
        choice = menu.get_choice()
        if choice == "1":
            play_1v1()
        elif choice == "2":
            show_matches()
        elif choice == "3":
            edit_match()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("That is not a valid option. Pick 1-5.")


main()
