import random


def play_game():
    # Define valid choices
    choices = ["stone", "paper", "scissors"]

    # Initialize win counters
    user_score = 0
    computer_score = 0

    print("=== Welcome to Stone, Paper, Scissors! ===")
    print("Rules: Stone beats Scissors | Scissors beats Paper | Paper beats Stone")
    print("Type 'quit' at any time to end the game.\n")

    while True:
        # 1. Get and validate player choice
        user_choice = (
            input("Enter your choice (stone, paper, scissors): ")
            .strip()
            .lower()
        )

        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("❌ Invalid input! Please enter stone, paper, or scissors.")
            continue

        # 2. Generate computer choice
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        # 3. Determine the round winner
        if user_choice == computer_choice:
            print(f"🤝 It's a tie! Both chose {user_choice}.")
        elif (
            (user_choice == "stone" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "stone")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print(f"🎉 You win this round! {user_choice.title()} beats {computer_choice}.")
            user_score += 1
        else:
            print(
                f"😢 Computer wins this round! {computer_choice.title()} beats {user_choice}."
            )
            computer_score += 1

        # 4. Display current standings
        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}\n")

    # Final wrap up when user quits
    print("\n================ Game Over ================")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("🏆 Congratulations! You beat the computer!")
    elif user_score < computer_score:
        print("🤖 Computer wins the overall match. Better luck next time!")
    else:
        print("🤝 The overall match is a tie!")
    print("Thanks for playing!")


# Run the game
if __name__ == "__main__":
    play_game()
