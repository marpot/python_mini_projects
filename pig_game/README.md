```markdown
# Dice Game: Race to 50

This is a multiplayer dice game where 2–4 players take turns rolling a die. The goal is to be the first player to reach or exceed a score of 50. Rolling a "1" ends the player's turn and resets their score for that turn to zero. The game features an interactive and competitive gameplay experience.

---

## How to Play

1. **Setup**:
   - Each player starts with a score of 0.
   - The first player to reach a total score of **50** wins.

2. **Gameplay**:
   - Players take turns rolling a six-sided die.
   - On their turn, they can choose to roll the die or end their turn:
     - **If the die shows 2–6**: Add the value to the current turn's score.
     - **If the die shows 1**: The player's turn ends immediately, and their score for the current turn resets to 0.
   - At the end of a turn, the player's total score is updated.

3. **Winning the Game**:
   - The game ends as soon as a player reaches or exceeds a score of 50.
   - If multiple players achieve the same highest score in the final round, the game results in a tie.

---

## Example

### Starting the Game
```plaintext
Enter the number of players(2 - 4): 3
```

### Player Turn
```plaintext
Player 1's turn has just started!
Your total score is: 12

Would you like to roll (y)? y
You rolled a 4
Your score this turn is: 4

Would you like to roll (y)? y
You rolled a 1! Turn done!
Player 1's total score is now: 12.
```

### Game End
```plaintext
Player 3 is the winner with a score of 50!
```

---

## Features

- **Multiplayer**: Supports 2–4 players.
- **Turn-Based Gameplay**: Each player takes turns rolling the die.
- **Randomized Rolls**: Simulates rolling a six-sided die using Python's `random` module.
- **Dynamic Scoring**: Tracks scores for each player and updates after each turn.
- **Win/Tie Detection**: Determines the winner or identifies a tie when scores are equal.

---

## Requirements

- Python 3.6+
- No external libraries are required.

---

## Running the Game

1. Save the script to a file, e.g., `dice_game.py`.
2. Run the script in a terminal or IDE:
   ```bash
   python dice_game.py
   ```

---

## Notes

- **Valid Input**: Ensure you input numbers for the player count (2–4) and `y` or `n` for rolling decisions.
- **Customizable**: Modify the `max_score` or adjust the dice range for unique gameplay.

---

Enjoy rolling your way to victory! 🎲
```