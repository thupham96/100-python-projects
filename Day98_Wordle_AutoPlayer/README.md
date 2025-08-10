# Day 98: Wordle Auto-Player — Selenium + Python

A small automation script that plays Wordle at **wordlegame.org**. It loads a 5-letter dictionary, chooses guesses using a letter-frequency heuristic, reads tile feedback (green/yellow/black), and filters candidates until it solves or runs out of attempts.

---

## Features

* Opens and plays at `https://wordlegame.org/` automatically
* Uses a **frequency-based scoring** heuristic to pick informative guesses
* Parses tile states (`correct/elsewhere/absent`) to narrow candidates
* Supports a fixed first guess (`heart` by default)
* Keeps Chrome open after the run for easy inspection

---

## How It Works (Quick Overview)

1. **Dictionary load**: reads `words_full.txt` and keeps only 5-letter alphabetic, lowercase words.
2. **Scoring**: for each candidate, sum the frequencies of its **unique** letters across all remaining candidates; pick the highest-scoring word.
3. **Feedback parsing**: map CSS classes to feedback:

   * `correct` → `g` (green, right letter & position)
   * `elsewhere` → `y` (yellow, right letter, wrong position)
   * `absent` → `b` (black/gray, not present — with a caveat for duplicates)
4. **Filtering**: remove words inconsistent with the feedback. For duplicate letters, a black can mean “no **additional** occurrences beyond confirmed greens/yellows.”

---

## Requirements

* Python 3.9+ recommended
* Google Chrome installed
* **ChromeDriver** that matches your Chrome version and is on your `PATH`
* Packages:

  ```bash
  pip install selenium
  ```

> If you don’t have ChromeDriver, download it from the official site matching your Chrome version and add it to your PATH (or place it next to the script).

---

## Project Structure

```
Day98_Wordle_AutoPlayer/
├── wordle_bot.py        # the script (code you provided)
└── words_full.txt       # 5-letter word list (lowercase, one per line)
```

**words\_full.txt**

* One word per line
* Lowercase
* Exactly 5 letters, alphabetic only

---

## Run It

```bash
python wordle_bot.py
```

The script will:

1. Launch Chrome and open the game
2. Click **Play**
3. Submit a guess each round (up to 6)
4. Print the chosen guess and stop when solved or if no candidates remain

---

## Configuration (in the script)

* **Starting word**:
  Change `initial_guess = "heart"` (must exist in `words_full.txt` to be used on attempt 0).
* **Delays**:
  `time.sleep(3)` waits are used for page settle/animations. Adjust if your machine/site is slow/fast.
* **Keep browser open**:
  `opts.add_experimental_option("detach", True)` keeps Chrome open after the script ends. Comment it out if you want the browser to close automatically.

---

## Notes & Troubleshooting

* **Fragile selectors**: this relies on site CSS classes:

  * Play button: `game__btn`
  * Rows: `Row`
  * Tiles: `Row-letter` with `correct/elsewhere/absent`
    If the site updates CSS, inspect the DOM (DevTools) and update class names accordingly.
* **Page timing**: if tiles read as `"s"` (unknown), the site hasn’t applied results yet. The script backs out and retries another guess. If this happens frequently, increase sleeps or replace with more granular `WebDriverWait` checks.
* **Driver mismatch**: version mismatch between Chrome and ChromeDriver causes startup failures. Make sure they match.
* **Dictionary quality**: a noisy or tiny word list hurts performance. Use a clean 5-letter English list.

---

## What I Learned

* Driving a browser with Selenium (navigation, clicks, typing, waits)
* Designing a simple **information-gain** heuristic with letter frequencies
* Translating UI state (CSS classes) into machine-readable feedback
* Handling duplicate-letter caveats in Wordle logic
* Iterative constraint filtering over a candidate set
