import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def play_game():
    result = "Heads"

    result = flip_coin()

    result = flip_coin() 
    result = flip_coin()

    result = "Computer" if result == "Heads" else "Opponent"

    return result

computer_wins = 0
opponent_wins = 0

for i in range(100):
    result = play_game()
    if result == "Computer":
        computer_wins += 1
    else:
        opponent_wins += 1

print("Results after 100 games:")
print(" Heads:", computer_wins)
print(" Tails:", opponent_wins)
