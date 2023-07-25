import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def play_game():
    computer_move1 = flip_coin()

    print("Your turn to play. Do you want to flip the coin? (y/n)")
    opponent_move2 = flip_coin() if input().lower() == 'y' else None

    computer_move3 = flip_coin()

    result = "Computer wins!" if computer_move3 == "Heads" else "You wins!"

    print("Computer's move 1:", computer_move1)
    print("your move 2:", "Heads" if opponent_move2 == "Heads" else "Tails") 
    print("Computer's move 3:", computer_move3)
    print(result)

play_game()
