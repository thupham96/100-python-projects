# ------------------------------------------------------------
# Wordle Auto-Player (Selenium)
# ------------------------------------------------------------
# - Opens https://wordlegame.org/
# - Loads a 5-letter dictionary from words_full.txt
# - Guesses a word each round using a frequency-based heuristic
# - Reads tile feedback (green/yellow/black) from the page
# - Filters the candidate word list accordingly
# ------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections
import time
from selenium.webdriver.chrome.options import Options

URL = "https://wordlegame.org/"

# ------------------------------------------------------------
# Load dictionary
# ------------------------------------------------------------
# Reads a local word list file and keeps only 5-letter alphabetic words.
# The list is used both for the initial candidate pool and for scoring.
with open("words_full.txt", encoding="utf-8") as f:
    DICT = []
    for line in f:
        word = line.strip().lower()
        if len(word) == 5 and word.isalpha():
            DICT.append(word)


# ------------------------------------------------------------
# Scoring heuristic
# ------------------------------------------------------------
# score_word() works by:
# 1) Counting letter frequencies in the remaining candidate words.
# 2) Assigning a score to a potential guess based on the sum of the
#    frequencies of its unique letters (set(word) avoids double-counting).
# 3) Choosing the word with the highest score tends to maximize
#    information gain (more green/yellow hits).
def score_word(word, remaining):
    counts = collections.Counter("".join(remaining))
    return sum(counts[c] for c in set(word))


# ------------------------------------------------------------
# Candidate filtering based on feedback
# ------------------------------------------------------------
# Feedback encoding per tile:
#   "g" -> green    : letter is correct and in the correct position
#   "y" -> yellow   : letter is in the word but in a different position
#   "b" -> black    : letter is not in the word (with caveat below)
#
# Important caveat for black:
# If a letter appears elsewhere in the guess with green/yellow feedback,
# then a black for the same letter means "no *more* occurrences than those
# already confirmed" (i.e., avoid excluding words with exactly that count).
def filter_candidates(cands, guess, feedback):
    new = []
    for w in cands:
        ok = True
        for i, (ch, fb) in enumerate(zip(guess, feedback)):

            # Green: must match the exact position.
            if fb == "g" and w[i] != ch:
                ok = False
                break

            # Yellow: letter must exist in the word, but NOT at this position.
            if fb == "y" and (ch not in w or w[i] == ch):
                ok = False
                break

            # Black: letter should not be present at all UNLESS it already
            # appeared in the guess as green/yellow (meaning limited count).
            if fb == "b":
                found_elsewhere = any(
                    gch == ch and gfb in ("g", "y")
                    for gch, gfb in zip(guess, feedback)
                )
                # If we haven't seen this letter as g/y anywhere else and
                # the candidate still contains it, reject the candidate.
                if not found_elsewhere and ch in w:
                    ok = False
                    break

        if ok:
            new.append(w)

    return new


# ------------------------------------------------------------
# Selenium setup
# ------------------------------------------------------------
opts = Options()
opts.add_experimental_option("detach", True)  # keep Chrome open after script ends
driver = webdriver.Chrome(options=opts)
driver.get(URL)
time.sleep(3)  # allow page to settle (simple fixed wait)

# Start the game by clicking the big "Play" button.
play_button = driver.find_element(By.CLASS_NAME, "game__btn")
play_button.click()

# Acquire a handle to the page body (we'll send keystrokes here).
board = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)
time.sleep(3)  # allow the game board to fully render


# ------------------------------------------------------------
# Main solve loop (max 6 attempts)
# ------------------------------------------------------------
cands = DICT[:]     # working copy of candidate words
attempt = 0

while attempt < 6:
    # Choose a guess:
    # - Use a fixed initial guess if it's in the candidate list
    # - Otherwise, pick the highest-scoring word from remaining candidates
    initial_guess = "heart"
    guess = (
        initial_guess
        if attempt == 0 and initial_guess in cands
        else max(cands, key=lambda w: score_word(w, cands))
    )

    print(guess)

    # Type the guess and submit
    board.click()
    for ch in guess:
        board.send_keys(ch)
    board.send_keys(Keys.ENTER)
    time.sleep(3)  # wait for tile animations / result

    # --------------------------------------------------------
    # Read feedback from the current row
    # --------------------------------------------------------
    rows = driver.find_elements(By.CLASS_NAME, "Row")
    tiles = rows[attempt].find_elements(By.CLASS_NAME, "Row-letter")

    fb_map = []
    for t in tiles:
        cls = t.get_attribute("class")
        if "absent" in cls:
            fb_map.append("b")
        elif "correct" in cls:
            fb_map.append("g")
        elif "elsewhere" in cls:
            fb_map.append("y")
        else:
            # "s" = still / unknown status (e.g., site lag or CSS change)
            fb_map.append("s")

    # Success: all five tiles are green
    if fb_map == ["g"] * 5:
        print(f"Solved with:{guess}")
        break

    # If all tiles are still "s", the site hasn't returned feedback yet.
    # Backspace to clear the row, drop this guess from candidates, and retry.
    if fb_map == ["s"] * 5:
        for _ in range(5):
            board.send_keys(Keys.BACKSPACE)
        cands.remove(guess)
        continue

    # Narrow the candidate pool using the feedback
    cands = filter_candidates(cands, guess, fb_map)
    if not cands:
        print("No candidates found.")
        break

    # If we reach the 6th attempt without success, it's a loss.
    if attempt == 5:
        print("You have lost!")

    attempt += 1


# Optional: close the browser when done.
# driver.quit()
