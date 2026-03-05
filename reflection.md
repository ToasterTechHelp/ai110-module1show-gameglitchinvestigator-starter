# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The hints were backwards — guessing too high told you to go higher. On every even attempt the secret got cast to a string, so comparisons broke completely (Python compares `"9" > "50"` alphabetically and gets it wrong). Hard mode used range 1–50, which is actually easier than Normal's 1–100. The UI also hardcoded "between 1 and 100" no matter the difficulty, and New Game always picked from 1–100 regardless of the selected mode.

---

## 2. How did you use AI as a teammate?

I used Claude Code throughout. It correctly caught the inverted hints right away — I verified by tracing `check_guess(70, 50)` and confirming it returned "Go HIGHER!" when it should say "Go LOWER!". It was misleading once: it suggested the Hard range (1–50) might be intentional since Hard has fewer attempts. That reasoning doesn't hold up — fewer guesses AND a smaller range makes the game easier, not harder. I rejected it and changed Hard to 1–200.

---

## 3. Debugging and testing your fixes

I only called a bug fixed when a test specifically targeting the broken behavior passed. For the inverted hints I wrote tests asserting the message contains "LOWER" when the guess is too high, and "HIGHER" when too low. For the string bug I tested `check_guess(9, 50)` — lexicographic comparison wrongly returns "Too High" there, but numeric returns "Too Low". Both tests failed before the fix and passed after.

---

## 4. What did you learn about Streamlit and state?

Every button click re-runs the entire script from the top, so without `st.session_state` the secret gets re-randomized on every interaction. The `if "secret" not in st.session_state:` guard sets it once and keeps it stable. Think of it like localStorage in a browser — it survives page reloads.

---

## 5. Looking ahead: your developer habits

Write tests around the broken behavior, not just the expected behavior — they double as regression guards. Next time I'd push back sooner when AI hedges with "this might be intentional." This project made it clear that AI code can look fine and still be subtly wrong; running it isn't enough, you have to trace it.
