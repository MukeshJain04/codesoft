import random

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
def play_game():
    global user_score, computer_score

    choices = ["rock", "paper", "scissors"]
    
    print("\n=== Rock, Paper, Scissors Game ===")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    
    while True:
        user_choice = input("\nYour choice (rock/paper/scissors): ").lower()

        if user_choice not in choices:
            print("❌ Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            result = "✅ You win!"
            user_score += 1
        else:
            result = "❌ You lose!"
            computer_score += 1

        # Display result and scores
        print(f"Result: {result}")
        print(f"🏆 Score: You {user_score} - {computer_score} Computer")

        # Ask to play again
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! 👋")
            break

# Run the game
play_game()
