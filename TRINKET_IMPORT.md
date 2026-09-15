# Trinket archive import

`python-fundamentals/`, `python-turtle/`, and `python-processing/` contain lessons curated from an
archive of roughly 309 Trinket projects (lesson drafts and student work) exported 2026-09-14. The
archive itself is not stored in this repo (see `.gitignore`); the review of it is preserved here.

## Methodology

Each project in the archive was reviewed for category (fundamentals / turtle / processing / pygame
/ data structures / other), code quality (clean / workable / broken-or-incomplete / trivial), and
reusability as standalone curriculum. Near-duplicate projects — many independent, near-identical
implementations of Turtle Race, Pong, spirographs, password generators, Fibonacci timers, and
number-guessing games — were consolidated to one representative each.

## What was included

76 files rated reusable, after deduplication, were copied into the folders below with minimal
renaming and no other edits:

- **`python-fundamentals/`** (28 files) — non-graphical: loops, functions, classes intro,
  recursion, sorting/linked-list basics. See its [README](python-fundamentals/README.md).
- **`python-turtle/`** (24 files) — turtle graphics: beginner shape exercises, fractals,
  spirographs, turtle races, a two-level tic-tac-toe. See its [README](python-turtle/README.md).
- **`python-processing/`** (23 files; the five needing images live in per-project folders) — a Processing-style
  drawing API distinct from `pygame/`: buttons, collision demos, Game of Life, Breakout, Pong,
  Dino Jump, Frogger, an OOP-focused aim trainer. See its [README](python-processing/README.md).
  This folder has no established conventions yet, unlike `pygame/` (see `CLAUDE.md`).

These files were copied with minimal renaming and were not rewritten for teaching style. A few have
since been edited — see [Post-import edits](#post-import-edits). They have not been verified to run
against a current environment beyond a syntax check: all 76 files parse under Python 3. Known
issues:

- `python-turtle/turtle_in_space.py` references `space.jpg` and `rocketship.png`, which are not
  present in the archive.
- Projects needing image assets were regrouped into per-project folders (code and images side by
  side) so their `loadImage(...)` calls resolve; the export's `assets/` nesting had broken them.
  An unused screenshot that shipped alongside `bouncing_ball.py` was deleted.
- Third-party sprites of unverified provenance ship in `python-processing/`: the Flappy Bird
  sprite, the Chrome offline-dino and its cactus, and a stock-photo turtle. Replace these before
  relying on the material publicly.
- No `LICENSE` file at the repo root.

All seven `loadImage(...)` calls in `python-processing/` have been confirmed to resolve against the
files sitting next to them.

## What was excluded

About 90 projects were empty files, syntax errors, unstarted stubs, or explicitly marked
work-in-progress. Roughly 140 more were individual lesson-session variants or near-duplicates of an
included file, retained in the archive for reference but not promoted as standalone curriculum.

A further set of projects — functional but messy, or more advanced than current lessons (heavy OOP,
several 1000+ line projects: Tetris, Tower Defense, Zombie Attack, Snake, Space Invaders variants)
— were rated as possible-but-unpolished candidates and left out of the curated folders. Several use
sprite-group/vector patterns beyond the scope of the current `pygame/` lessons and could seed more
advanced material.

## Post-import edits

Reviewed 2026-09-14 before publishing. Apart from the following, the curated files remain as
imported:

- **Removed a student's first name.** `python-turtle/flower_maker.py` credited a remix to a named
  student; it now reads "Remixed from a student's code". No other student names appear in the
  curated folders — of the 63 student-named projects in the archive, only one was promoted at all
  (an instructor-authored starter, now `python-processing/flappy_bird_starter.py`), and the name
  was dropped in the rename. The archive itself is gitignored and has never been committed.
- **Removed the employer/school line** from the author headers of the four
  `python-turtle/turtle_race*` files, leaving the `Author:` line unchanged.
- **Fixed Python 2 prints.** `python-fundamentals/python_practice_problems_level_1.py` lines 85, 87
  and 88 converted from `print x` to `print(x)`, keeping the existing `str()` concatenation rather
  than introducing f-strings. The file now runs and reports `0/10 passed` — which is correct: its
  functions are unfilled `pass` stubs by design, and the harness is what a student runs to check
  their work.

## Layout

- Archive: `2026-09-14-trinket-export/` (gitignored, local only)
- Curated lessons: `python-fundamentals/`, `python-turtle/`, `python-processing/`
