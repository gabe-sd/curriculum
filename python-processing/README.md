# python-processing

Lessons using a Processing-style (p5-for-python) drawing API: buttons, collision demos, Conway's
Game of Life, Breakout, Pong, Dino Jump, Frogger, and an OOP-focused aim trainer. Sourced from an
archive of Trinket projects — see [`TRINKET_IMPORT.md`](../TRINKET_IMPORT.md) for provenance. Files
are unedited pulls (renamed only) and have not been rewritten to match a specific teaching style.
Unlike `pygame/`, this folder has no established conventions yet (see `CLAUDE.md`). The original
Processing-for-Python library/environment these were written against is unknown; check
compatibility with whichever library is installed before running them.

| file | what it is | notes |
|---|---|---|
| `inverted_squares_basic_example.py` | Tiny mouseX/mouseY-driven shape demo | good intro-to-processing snippet |
| `mouse_2d_example.py` | Port of the classic Processing "Mouse 2D" example | clean |
| `moving_rectangle.py` | Click-to-move rectangle, with a commented-out auto-move alternative | good state/event intro |
| `button_function.py` | Reusable, documented `button()` function | good template for a "GUI button" lesson |
| `image_button_function.py` | Reusable image-button function | modular lesson snippet, pairs with `button_function.py` |
| `oop_dot_example.py` | Small class + animation example (bouncing dots) | simple OOP-in-processing demo |
| `collision_function_demo.py` | Rect-collision + class-instance-list pattern | well-commented teaching demo |
| `fading_circle.py` | Alpha-fade animation using `frameCount` | minimal animation example |
| `pulsing_circle.py` | Mouse-driven pulsing circle with color cycling | small, clean "juicy" visual-effects example |
| `rainbow_grid.py` | Nested-loop 2D grid colored by mouse position + time | nice nested-loops/2D-lists example |
| `bouncing_ball.py` | Basic bounce-off-walls physics | *has a `bouncing_ball_assets/` folder alongside it (one screenshot, not required to run)* |
| `game_of_life.py` | Working Conway's Game of Life | only fully-functional version out of 4 attempts in the export |
| `aim_labs_oop_intro.py` | Click-to-score aim trainer, explicitly framed as an "OOP Intro" | clean Ball class, best of several Aim Labs variants |
| `solar_system_simulation.py` | Orbit/rotation demo (`translate`/`rotate`) | clean, well-commented, no image assets needed |
| `squid_game_rotation_example.py` | Red-Light-Green-Light game demoing `rotate()`/`pushMatrix` | complete, well-commented, example-driven as the title suggests |
| `jump_game.py` | Minimal gravity/jump mechanic | *needs `jump_game_assets/turtle.png` to run* |
| `dino_jump.py` | Dino-runner clone: obstacle class, collision, scoring, game over | most complete of ~6 dino-game attempts in the export; *needs `dino_jump_assets/` (cactus/dino images)* |
| `flappy_bird_starter.py` | Flappy Bird starter with heavy scaffolding comments and an explicit "NEXT:" prompt | reads like a teacher-authored starter, not a finished game; *needs `flappy_bird_starter_assets/`* |
| `frogger.py` | Frogger clone: cars, collision, win/lose | best-organized of several Frogger attempts; has commented-out debug hitbox code worth keeping for teaching |
| `atari_breakout_finished.py` | Complete Breakout: bricks, paddle bounce physics, game over | best of ~6 Breakout attempts in the export |
| `pong.py` | Pong vs. a simple AI paddle, with scoring | clean OOP Paddle/Ball structure |
| `infection_spread_simulation.py` | "Infection spread" simulation using a Ball class + collision checks | interesting simulation/algorithms angle, not just a game |
| `rock_paper_scissors_gui.py` | Image-button RPS with streak tracking and animation timing | *needs `rock_paper_scissors_gui_assets/` (included alongside it — cactus/dino/turtle images)* |

Several files reference image assets that came along in the export (now sitting in `_assets`
subfolders next to them). Every `loadImage(...)` call has been checked against its `_assets` folder
and all of them resolve; the one exception is `bouncing_ball_assets/`, which holds a screenshot of
the program's output that `bouncing_ball.py` never loads.

Note that these sprites are third-party images of unverified provenance — the Flappy Bird sprite,
the Chrome offline-dino and its cactus, and a stock-photo turtle. Swap in your own art before
relying on this material publicly.

Bigger, messier games (Tetris, Tower Defense, Zombie Attack, Snake, Space Invaders variants) that
are functional but need real cleanup, plus many near-duplicate lesson-session variants, were not
included here.
