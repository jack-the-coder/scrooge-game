import os


def printscrooge():
    os.system("clear")
    print("Welcome to Scrooge! \nThis game quits if given bad input.")
    print("\nPress Enter to continue...")
    input()

def print_question(question, option0, option1, option2, option3):

    print(question)
    print("A: " + option0)
    print("B: " + option1)
    print("C: " + option2)
    print("D: " + option3)
    answer = input("Choice: ")
    if answer.upper() == "A":
        return "A"
    elif answer.upper() == "B":
        return "B"
    elif answer.upper() == "C":
        return "C"
    elif answer.upper() == "D":
        return "D"
    else:
        print("Error 0: Bad input. Quitting.")

def start_of_game():
    os.system("clear")
    print("You are in your counting-house. ")
    answer0 = print_question(
        "What do you wish to do?",
        "Look over at Bob",
        "Count your money",
        "Do nothing",
        "Give Bob a raise",
        )

    if answer0 == "A":
        print("You reluctantly turn your head over towards Bob.")
    elif answer0 == "B":
        print("You have no idea how much money you have. That's Bob's job.")
    elif answer0 == "C":
        print("You do nothing.")
    elif answer0 == "D":
        print("You would never do that. You're Scrooge!")


printscrooge()
start_of_game()
