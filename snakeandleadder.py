import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll, snakes, ladders):
    position += roll
    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}. Go down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder at {position}. Go up to {ladders[position]}")
        position = ladders[position]
    return position

def main():
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 2}
    ladders = {9: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    positions = [0, 0] 
    player = 0

    while True:
        input(f"\nPlayer {player+1}'s turn. Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"Player {player+1} rolled a {roll}")
        positions[player] = move_player(positions[player], roll, snakes, ladders)
        print(f"Player {player+1} is now at position {positions[player]}")
        if positions[player] >= 100:
            print(f"\nPlayer {player+1} wins!")
            break
        player = 1 - player

if __name__ == "__main__":
    main()

