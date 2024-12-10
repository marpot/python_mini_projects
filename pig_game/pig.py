import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players(2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <=4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print('Invalid, try again.')

max_score = 50
players_scores = [0 for _ in range(players)]   

while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!")
        print(f"Your total score is: {players_scores[player_idx]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ").strip().lower()
            if should_roll != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            
            print(f"Your score this turn is: {current_score}")
            
        players_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {players_scores[player_idx]}.")


max_score = max(players_scores)
winners = [idx + 1 for idx, score in enumerate(players_scores) if score == max_score]

if len(winners) > 1:
    print(f"\nIt's a tie! Players {', '.join(map(str, winners))} win with a score of {max_score}!")
else:
    print(f"\nPlayer {winners[0]} is the winner with a score of {max_score}!")