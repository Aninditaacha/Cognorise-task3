import random

def get_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    while user_choice not in valid_choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    return user_choice

def get_computer_choice():
    valid_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(valid_choices)

    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if winner == "user":
        print("You win!")
    elif winner == "computer":
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            break

if __name__ == "__main__":
    main()