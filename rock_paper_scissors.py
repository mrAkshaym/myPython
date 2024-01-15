import random as ra

option = ["rock", "paper", "scissors"]

def game():
    user_choice = input("Enter your choice rock, paper or scissors: ")
    computer_choice = ra.choice(option)
    print("Computer choice is", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win")
    else:
        print("You lose")

    
if __name__ == "__main__":
    game()
