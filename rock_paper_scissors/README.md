```markdown
# Rock Paper Scissors Game

This is a simple text-based Rock, Paper, Scissors game where you can play against the computer. The game will keep track of your wins, the computer's wins, and draws until you decide to quit.

---

## How to Play

1. Run the script in your terminal or IDE.
2. You will be prompted to enter your choice of either "Rock", "Paper", or "Scissors".
3. The computer will randomly choose one of the three options.
4. The winner is determined based on the traditional rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
5. You can also enter "Q" to quit the game at any time.

---

## Example Gameplay

### Start:
```plaintext
Type Rock/Paper/Scissors or Q to quit.
```

### User's Input and Game Response:
```plaintext
Type Rock/Paper/Scissors or Q to quit. rock
Computer picked scissors.
You won!
```

### In Case of a Draw:
```plaintext
Type Rock/Paper/Scissors or Q to quit. paper
Computer picked paper.
draw!
```

### Final Score:
```plaintext
You won 3 times.
Computer wins 2 times.
Draws: 1
Goodbye!
```

---

## Features

- **Interactive Gameplay**: The game prompts you for input, and responds based on the game's rules.
- **Score Tracking**: The number of wins for both the user and the computer, as well as the number of draws, are tracked throughout the game.
- **Quit Option**: You can type "Q" at any time to quit the game and see the final score.

---

## Requirements

- Python 3.6+.

---

## How to Run

1. Save the script as a `.py` file, for example `rock_paper_scissors.py`.
2. Run the script in your terminal or IDE:
   ```bash
   python rock_paper_scissors.py
   ```

---

## Notes

- The game uses a random number generator for the computer's choice of Rock, Paper, or Scissors.
- The game will continue until you enter "Q" to quit.

---

Enjoy the game and may the best player win! 🎮✌️
```