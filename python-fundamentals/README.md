# python-fundamentals

Non-graphical Python lessons and exercises: loops, functions, classes, recursion, and basic
algorithms (sorting, linked lists). Sourced from an archive of Trinket projects — see
[`TRINKET_IMPORT.md`](../TRINKET_IMPORT.md) for provenance. Files are near-verbatim pulls (renamed
only, apart from a Python 2 `print` fix in `python_practice_problems_level_1.py`) and have not been
rewritten to match a specific teaching style.

| file | what it is | notes |
|---|---|---|
| `beginner_exercises_1.py` | Numbered intro exercises: print/input/random/guessing game | clean, good day-1 material |
| `guessing_game.py` | Classic "guess the computer's number" loop | clean |
| `number_guessing_game_level_1.py` | Simpler variant of the above, "Level 1" framing | near-duplicate of `guessing_game.py`, pick one |
| `number_guessing_game_vs_bot.py` | Computer guesses via binary search (halving) | good algorithmic-thinking companion |
| `number_guessing_bot.py` | "Bot guesses your number" — pairs well with `guessing_game.py` (roles reversed) | |
| `ai_guesses_your_number.py` | Another binary-search bot-guesses-your-number variant | near-duplicate of `number_guessing_bot.py`, pick one |
| `bot_number_guesser.py` | Yet another binary-search variant, cleanest of that family | near-duplicate — of the three bot-guesser files, this and `number_guessing_bot.py` are the strongest candidates; drop the others |
| `dice_roller.py` | Dice roll loop with running total | clean |
| `simple_calculator.py` | if/elif calculator via menu | clean |
| `calculator_with_error_handling.py` | Calculator with try/except and a menu loop | near-duplicate of `simple_calculator.py`, more robust |
| `classes_demo.py` | Short intro-to-OOP demo | good seed for a gated "classes" lesson (per pygame/ convention, OOP is advanced-only) |
| `if_elif_else_demo.py` | Grade classifier | tiny, clean, does what it says |
| `modulus_operator_demo.py` | Modulus operator demo | tiny, clean |
| `sum_range_function.py` | Function that sums over a range | tiny |
| `recursive_countdown.py` | Minimal recursion example | tiny, pairs with `recursion_exercises.py` |
| `recursion_exercises.py` | Recursive vs. iterative countdown, with self-test asserts | clean |
| `functions_as_values_demo.py` | Functions passed around as values | purpose-built concept demo |
| `username_helper.py` | Practical strings/lists/loops exercise | clean, no graphics |
| `madlibs.py` | Mad Libs using lists/input | uses raw ANSI escape codes for bold/underline — may not render in all terminals, worth checking |
| `tic_tac_toe_text_based.py` | Full 2-player text tic-tac-toe with win/tie/play-again logic | best of several text-based tic-tac-toe attempts in the export |
| `password_generator_starter.py` | Starter scaffold (letter/number/symbol lists) | intentionally incomplete — meant as a starting point, not a finished lesson |
| `python_practice_problems_level_1.py` | Fill-in-the-function worksheet with a built-in test harness | runs as-is; reports `0/10 passed` until the student fills in the `pass` stubs |
| `algorithms_exercises.py` | Unsolved algorithm exercise with asserts | pairs with `algorithms_exercises_solutions.py` |
| `algorithms_exercises_solutions.py` | Worked solution to the above | |
| `fibonacci_timing.py` | Naive vs. memoized Fibonacci with timing comparison | clean, best of several Fibonacci/timing variants in the export |
| `linked_list.py` | Full linked-list class (add/remove/index/length) | known bugs listed at the top of the file |
| `merge_sort.py` | Merge sort with teaching print-tracing and a random-test harness | |
| `merge_sort_starter.py` | Stub version of merge sort with the same test harness | pairs with `merge_sort.py` as starter/solution |

Additional functional-but-messier candidates and personal-lesson variants were not included here.
