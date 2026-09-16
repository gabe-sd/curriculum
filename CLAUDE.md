# curriculum

Lessons for teaching middle- and high-school students (ages ~10–17) who have done basic Python (usually `turtle`), maybe text-based games or Scratch. Assume a 12-year-old is reading the code.

## Working with me

Keep answers short and plain. Lead with the verdict or the answer; skip the write-up that
produced it. When I ask to see a file, show it — don't attach an analysis. Don't restate
findings I already have.

## Git

Use a separate commit for new work and leave history intact. Rewrite history only to remove
personal information, and only while the branch is still unpushed (check `git branch -vv`).
Don't push unless I say to.

## Student privacy

`2026-09-14-trinket-export/` is a local, gitignored archive of ~309 exported Trinket projects.
63 are named after students, several with full names of minors. Never commit it or un-ignore it.

When promoting any file out of it into the curriculum, check the source project name and the
file's own comments and docstrings for names first. Scan docstrings, not just `#` comments.

## Structure

This repo is organized by subject, one folder per subject. Currently:

- `python-pygame/` — pygame game-programming lessons. The conventions below are specific to this folder.
- `python-fundamentals/` — non-graphical: loops, functions, recursion, sorting, text games.
- `python-turtle/` — turtle graphics: shapes, fractals, spirographs, turtle races.
- `python-processing/` — Processing-style drawing API (`setup()`/`draw()`/`run()`). Projects needing images get their own folder with the images beside the code.

The three `python-*` folders were imported from a Trinket archive and haven't been normalized. Each has a README describing its files. Match whatever file you're editing rather than applying the pygame rules to them.

## showcase/

Finished student projects kept as exemplars — things to show students as "you could build this."
They live in `<subject>/showcase/` (currently `python-turtle/` and `python-processing/`). They are
not lessons and are not part of any progression.

- **Files go in unedited.** Byte-identical to the source. Do not add a header, do not add or
  reword comments, do not rename variables, do not clean anything up, do not fix style. A file
  that needs edits to run does not belong in `showcase/`.
- **Never write anything into these files addressed to the teacher.** This is a public repo.
  Notes about what was or wasn't changed go in the commit message.
- What a project is and which concepts it shows go in the subject's README table, not in the file.
- A project needing images or a second module gets its own folder, entry point `main.py`, assets
  beside the code. Nothing else from the export is copied in — no `metadata.json`.
- Anonymous, always. Before promoting anything, check the source project name and the file for
  names: comments, docstrings, string literals, and variable names. See "Student privacy" above.
- Which projects get promoted is a teacher decision, like any other curriculum decision.

## python-pygame/

### Dependencies

Vanilla Python + `pygame` only. Standard-library modules (e.g. `random`) are fine. No other third-party libraries.

### File conventions

- Files live in `python-pygame/`, named `<game>_part<N>.py`. Each part builds on the prior — keep the earlier code and its teaching comments intact; add to them.
- Top of file: banner comment with `# ===` borders, game name, part number, controls.
- Part 2+: include a `# ===== NEW IN PART N =====` summary block near the top, and mark each added block inline with `# ===== NEW IN PART N: ... =====`.
- Section dividers: `# --- Section ---` (major), `# -- subsection --` (minor).

### Code style

- Functions are fine when they genuinely help a student understand the code. Don't introduce them just for tidiness.
- Constants `UPPER_CASE` (`WHITE`, `WINNING_SCORE`). Variable names descriptive (`paddle1`, not `p1`).
- File order: imports → `pygame.init()` → window / clock / colors / font → game objects and state → game loop → `pygame.quit()`.
- Game loop order: events → held keys → update → draw → `display.flip()` → `clock.tick(60)`.
- `pygame.Rect` for positions, `colliderect` for collisions.
- `str(x)` over f-strings unless f-strings have been taught.

### Commenting style

Comments teach. Explain *why* and introduce pygame concepts in plain language. Keep inline reminders for easily-forgotten bits (e.g. `# (R, G, B) from 0-255` near a color, `# pygame.Rect(x, y, w, h)` near a Rect). Err toward more explanation than production code.

### What NOT to do

- Don't use Python features the student hasn't seen: list comprehensions, ternaries, dataclasses, type hints, walrus, decorators.
- Don't remove or condense teaching comments.
- Don't add features beyond the lesson's scope, even if obvious.
- Don't create new lesson files unprompted — curriculum decisions come from the teacher.

### Pygame lesson progression

- `pong_part1.py` — two-player Pong. Window, game loop, `Rect`, `key.get_pressed()`, `colliderect`, text rendering, scoring.
- `pong_part2.py` — win condition, post-point pause via `pygame.time.get_ticks()`, game over + restart. Introduces `KEYDOWN`, game state flag, timestamp pausing.
- `flappybird_part1.py` — Flappy Bird. Lists of objects, `for` loops over lists, `append`/`pop`, gravity, `random.randint`, frame-counter timer.
