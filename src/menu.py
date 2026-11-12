def show_menu():
    print("")
    print("=== ROCK PAPER SCISSORS")
    print("1. Play 1v1")
    print("2. View Match History")
    print("3. Edit a match")
    print("4. Exit")


def get_choice():
    show_menu()
    choice = input("Choose an option: ")
    return choice
