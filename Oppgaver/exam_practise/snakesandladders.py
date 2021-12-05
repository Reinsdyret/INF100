"""Earlier exam task, a simple board game"""
from collections import Counter
import random

def roll_dice():
    """Roll dice getting number from [1,2,...,6]"""
    return random.randint(1,6)

def player_cross_0(startpos:int, diceroll:int) -> bool:
    """Returns True if player has crossed 0, False if not"""
    return 15 < startpos + diceroll

def simulate(rounds:int):
    """Simulate an amount of rounds and print end positions in percentage and how many players managed x rounds"""
    # Init variables
    PLAYERS = 100000
    board = {
        0: 0,
        1: 1,
        2: 2,
        3: 8,
        4: 4,
        5: 5,
        6: 6,
        7:7,
        8:8,
        9:13,
        10:2,
        11:11,
        12:12,
        13:13,
        14:14,
        15:6
    }

    # Create lists for keeping track of round gone and position of players
    players_rounds = [0 for i in range(PLAYERS)]
    players_positions = [0 for i in range(PLAYERS)]

    # Simulate rounds
    for _ in range(rounds):
        for player in range(PLAYERS):
            position = players_positions[player]
            dice_roll = roll_dice()
            new_position = board[(position + dice_roll) % 15]
            players_positions[player] = new_position
            if player_cross_0(position,dice_roll):
                players_rounds[player] += 1
    
    # Print player positions for percentage
    percentages = []
    for position in range(16):
        counter = 0
        for player_position in players_positions:
            if player_position == position:
                counter += 1
        percentage = 100/PLAYERS * counter
        percentages.append(str(round(percentage)))
    print(" ".join(percentages))

    # Print how many players managed x rounds
    max_rounds = max(players_rounds)
    rounds_counter = Counter(players_rounds)
    for rounds in range(max_rounds):
        count = rounds_counter[rounds]
        percentage_rounds =round(100 / sum(rounds_counter.values()) * count)
        print(f"{count:>5} players managed {rounds} rounds ({percentage_rounds} %)")


simulate(20)
