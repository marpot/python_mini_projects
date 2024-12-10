```markdown
# Number Guessing Game

A fun and interactive number guessing game built with Python! Try to guess the randomly generated number within the specified range, and the game will guide you by letting you know if your guess is too high or too low.

---

## Features

- **Dynamic Range**: You decide the upper limit of the range.
- **Random Number Generation**: The game generates a random number within your specified range.
- **Hints Provided**: Get feedback if your guess is too high or too low.
- **Track Attempts**: The game keeps count of your guesses.

---

## How to Play

1. **Run the Script**:
   - Save the script as `number_guessing_game.py`.
   - Run the script in your terminal or command prompt:
     ```bash
     python number_guessing_game.py
     ```

2. **Set the Range**:
   - Enter a positive number when prompted. This will set the upper limit of the guessing range. For example:
     ```plaintext
     Type a number: 50
     ```
   - The game will generate a random number between 0 and the number you chose.

3. **Make Guesses**:
   - Enter guesses to try to find the random number.
   - The game provides feedback:
     - `"You were above the number"` if your guess is too high.
     - `"You were below the number!"` if your guess is too low.

4. **Win the Game**:
   - Keep guessing until you find the correct number.
   - The game will congratulate you and display the number of attempts you made.

---

## Example Gameplay

```plaintext
Type a number: 100
Make a guess: 50
You were above the number
Make a guess: 25
You were below the number!
Make a guess: 30
You got it!
You got it in 3 guesses
```

---

## Customization

- **Change Range**: Modify the script to set a default range if no input is provided.
- **Add Difficulty Levels**: Introduce predefined ranges (e.g., Easy, Medium, Hard).
- **Enhance Feedback**: Provide more descriptive hints (e.g., "You are very close!").

---

## Dependencies

- **Python Standard Library**: The script uses the `random` module, which is built into Python.

---

## Notes

- Ensure that the input for the range is a positive integer greater than 0.
- Only numeric guesses are accepted.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and share it!

---

Enjoy the guessing game and see how many attempts it takes to win! 🎲
```