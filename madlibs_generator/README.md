```markdown
# Interactive Story Customizer

Create your own version of a story by filling in the blanks with custom words! This Python script reads a story from a file, identifies placeholders (e.g., `<name>`, `<adjective>`), and lets you replace them with your chosen words to personalize the tale.

---

## Features

- **Dynamic Placeholders**: Detects all words wrapped in `< >` from the story.
- **Interactive Input**: Prompts the user to input custom words for each placeholder.
- **Customizable Story**: Replaces placeholders with user-provided words and displays the completed story.

---

## How to Use

1. **Prepare Your Story**:
   - Create a text file named `story.txt` in the same directory as the script.
   - Add a story with placeholders wrapped in `< >`, such as:
     ```text
     Once upon a time, there was a <adjective> <animal> who lived in a <place>.
     ```

2. **Run the Script**:
   - Save the script as `story_customizer.py`.
   - Run the script using:
     ```bash
     python story_customizer.py
     ```

3. **Fill in the Blanks**:
   - When prompted, enter words to replace each placeholder.

4. **View Your Story**:
   - The script will print the customized story to the console.

---

## Example

### Input (`story.txt`):
```text
Once upon a time, there was a <adjective> <animal> who loved to <verb> in the <place>.
```

### Interactive Session:
```plaintext
Enter a word for <adjective>: brave
Enter a word for <animal>: lion
Enter a word for <verb>: explore
Enter a word for <place>: jungle
```

### Output:
```plaintext
Once upon a time, there was a brave lion who loved to explore in the jungle.
```

---

## Customization

- **Change Placeholders**: Update `story.txt` to use different or additional placeholders.
- **Enhance Input**: Add validation for specific word types (e.g., ensure `<adjective>` is truly descriptive).

---

## Dependencies

- **Python Standard Library**: No additional libraries are required.

---

## Notes

- Placeholders in the story must be enclosed in `< >` to be recognized by the script.
- Ensure the `story.txt` file is in the same directory as the script.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and share it!

---

Enjoy crafting your own stories! 📚✍️
```