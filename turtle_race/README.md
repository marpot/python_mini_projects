```markdown
# Turtle Racing Game

A fun racing game built using Python's `turtle` module! Players can choose the number of racers (2-10), and the colorful turtles will race to the finish line. The first turtle to cross the finish line wins!

## Features
- **Interactive Setup**: Choose the number of racers (2-10).
- **Colorful Racing**: Turtles are assigned random vibrant colors.
- **Random Movement**: Each turtle moves a random distance on every turn, making the race unpredictable and exciting.
- **Visual and Console Output**: Watch the race unfold on the screen and see the winner announced in the console.

---

## How to Run

1. **Install Python**: Make sure Python is installed on your system.
2. **Download the Script**: Save the script as `turtle_racing.py`.
3. **Run the Script**: Open your terminal or command prompt and execute:
   ```bash
   python turtle_racing.py
   ```
4. **Follow the Prompts**: Enter the number of racers when prompted.

---

## Game Flow

1. **Setup**:
   - The program initializes a `turtle` window with dimensions 700x700.
   - Turtles are placed at the starting positions, spaced evenly across the screen.

2. **The Race**:
   - Turtles move forward a random distance on each step.
   - The race continues until one turtle crosses the finish line (top of the screen).

3. **Winner Announcement**:
   - The winning turtle's color is printed in the console.

---

## Customization

- **Screen Dimensions**: Change the `WIDTH` and `HEIGHT` constants to adjust the screen size.
- **Turtle Colors**: Modify the `COLORS` list to add or remove turtle colors.

---

## Example Output

### Console:
```plaintext
Enter the number of racers (2 - 10): 5
The winner color is: blue
```

### Screen:
- A visual race with colorful turtles competing to cross the finish line.

---

## Dependencies

- **Python Standard Library**: The script only uses built-in modules (`turtle`, `time`, `random`).

---

## License

This project is open-source and available under the MIT License. Feel free to modify and share it!

---

Enjoy the race! 🐢🏁
```