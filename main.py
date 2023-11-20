import random

def get_user_choice():
    # Function to get the user's choice with input validation
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    # Function to get a random choice for the computer
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner based on the game rules
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_name = input("Enter your name: ")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n{user_name.title()} chose {user_choice}")
        print(f"The computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores based on the result
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        # Display the current score
        print(f"Score - {user_name}: {user_score}  Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
