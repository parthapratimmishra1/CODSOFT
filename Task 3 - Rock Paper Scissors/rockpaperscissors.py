import random


choices = ['rock', 'paper', 'scissors']

your_score = 0
computer_score = 0

print(" Welcome to Rock-Paper-Scissors Game!")

while True:
    print("\nChoose rock, paper, or scissors")
    user = input("Your choice: ").lower()

    if user not in choices:
        print(" That's not a valid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f" Computer chose: {computer}")

  
    if user == computer:
        print(" It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print(" You win this round!")
        your_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1

    print(f" Score → You: {your_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n Final Score:")
        print(f"You: {your_score} | Computer: {computer_score}")
        print("Thanks for playing! ")
        break
