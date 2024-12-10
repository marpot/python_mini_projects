import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the speed typing test!')
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)  # Wyświetlenie tekstu docelowego
    stdscr.addstr(1, 0, f"WPM: {wpm}")  # Wyświetlenie WPM na górze ekranu

    # Wyświetlenie obecnie wpisywanego tekstu
    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addstr(2, i, char, curses.color_pair(1))  # Zielony, gdy poprawny
        else:
            stdscr.addstr(2, i, char, curses.color_pair(2))  # Czerwony, gdy błędny

def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    wpm = 0

    # Ustawienie zegara do obliczania WPM
    stdscr.nodelay(True)
    start_time = time.time()

    while True:
        elapsed_time = max(time.time() - start_time, 1)  # Uniknięcie dzielenia przez 0
        wpm = round((len(current_text) / 5) / (elapsed_time / 60))

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except curses.error:  # Obsługujemy tylko błędy specyficzne dla curses
            continue

        if ord(key) == 27:  # Escape w ASCII
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        # Koniec testu po zakończeniu wprowadzania
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)
    stdscr.addstr(3, 0, "You completed the test! Press any key to exit.")
    stdscr.getkey()

wrapper(main)
