def main():
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print('*' * score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")

def get_valid_score():
    score = int(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100.")
        score = int(input("Enter a score (0-100): "))
    return score

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()