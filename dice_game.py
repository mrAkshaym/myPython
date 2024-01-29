import random

def play_dice_game():
    print("Who ever rolls the dice and gets a 6 first wins")
    print(" Press r to roll")
    print(" Press q for input to quit midway. The one that quits loses.")
    turn = 'r'
    dice = 0
    player1 = input(" Enter name of the first player ")
    player2 = input(" Enter name of the second player ")

    print("Player 1 starts ...")
    while (turn =='r'):
        message = player1 + " please press 'r' to roll the dice."
        turn = input(message);
        print(turn)
        if (turn == 'r'):
            dice = str(random.randint(1,6))
            print(player1+"'s dice rolled for",dice)
        elif (turn =='q'):
            print(player2, " wins.")
            break
        else:
            print(player1, " entered incorrect input. Loses their turn.")

        if (dice == '6'):
            print(player1, " wins.")
            break

        message = player2 + " please press 'r' to roll the dice."
        turn = input(message);
        if (turn == 'r'):
            dice = str(random.randint(1,6))
            print(player2+"'s dice rolled for",dice)
        elif (turn =='q'):
            print(player1, " wins.")
        else:
            print(player1, " entered incorrect input. Loses their turn.")

        if (dice == '6'):
            print(player2, " wins.")
            break

         
def main():
    play_dice_game()

main()
