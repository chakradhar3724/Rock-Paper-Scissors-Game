import random
options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice from rock (or) paper (or) scissors: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a TIE")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You WIN")
    else:
        print("You LOSE")

    play_again = input("Play again? (Y/N): ").upper()
    if play_again != "Y":
        running = False

print("Thanks for Playing")
          