import random

def get_computer_choice():
    """Return the computer's random choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def game():
    """Play the Rock, Paper, Scissors game."""
    print("Rock, Paper, Scissors Game")
    print("-------------------------------")
    print("Instructions:")
    print("1. Enter 'rock', 'paper', or 'scissors' to make a choice.")
    print("2. Type 'quit' to exit the game.")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nUser choice: {user_choice}")
        print(f"Computer choice: {computer_choice}\n")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print(f"It's a tie!")
        elif winner == 'user':
            print(f"{user_choice.capitalize()} beats {computer_choice}! You win this round.")
            user_score += 1
        else:
            print(f"{computer_choice.capitalize()} beats {user_choice}! Computer wins this round.")
            computer_score += 1

        print(f"\nScore - User: {user_score}, Computer: {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    game()
