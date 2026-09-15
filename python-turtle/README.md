# python-turtle

Turtle-graphics lessons: beginner shape exercises, fractals, spirographs, turtle races, and a
two-level tic-tac-toe. Sourced from an archive of Trinket projects — see
[`TRINKET_IMPORT.md`](../TRINKET_IMPORT.md) for provenance. Files are near-verbatim pulls (renamed
only, apart from the attribution edits noted there) and have not been rewritten to match a specific
teaching style.

| file | what it is | notes |
|---|---|---|
| `teaching_with_turtle_intro.py` | Intro demo: functions, circles, text | explicitly written as a teaching file |
| `beginner_exercise_1_square_spiral.py` | Beginner exercise: draw a square, then a spiral | short, clean, well-scoped |
| `beginner_exercise_2_flower.py` | Follow-on beginner exercise: squarish flower | same style as exercise 1 |
| `draw_square_function.py` | Parameterized `draw_square(x, y, size)` function | good functions+turtle intro |
| `n_sided_shape_loop.py` | Function draws an n-sided polygon, reused in a loop | minimal functions+loops example |
| `circles_spiral_simple.py` | Simple circle spiral using `input()` | tiny, clean |
| `infinite_colored_shapes.py` | Infinite loop of randomly colored polygons | combines loops/random/color |
| `flower_maker.py` | Randomized flower generator with color-list popping | best of several flower-drawing variants in the export |
| `pixel_art_mushroom.py` | Pixel-art mushroom drawn from a 2D list grid | nice combined lists+turtle lesson |
| `spider_web.py` | Loop-based spirograph-style web pattern | clean, simple |
| `spirograph.py` | Spirograph with user-chosen angle and background color | best of ~6 near-identical spirograph variants in the export |
| `spirograph_with_user_input.py` | Simpler spirograph, angle via `input()` | distinct enough from `spirograph.py` to keep both |
| `spiral_n_sided_shape_user_input.py` | Spiral of an n-sided shape, size/sides from user input | distinct concept from the spirograph family |
| `star_fractal.py` | Recursive fractal star | good intro-to-recursion turtle lesson |
| `fractal_tree.py` | Recursive fractal tree | pairs with `star_fractal.py` and `h_fractal.py` as a mini recursion unit |
| `h_fractal.py` | Recursive H-fractal | well-commented base case / recursive step |
| `tree_fractal.py` | Another recursive fractal tree | distinct implementation from `fractal_tree.py` — compare and pick, or keep both for variety |
| `tic_tac_toe_mouse_click.py` | Mouse-click tic-tac-toe board (no win-check yet) | well-structured, good base to build win-checking onto |
| `tic_tac_toe_level_2.py` | Polished mouse-click tic-tac-toe with win-check and input validation | header credits Gabriel Venditti — appears to be an instructor reference implementation |
| `turtle_race_2_0.py` | Turtle Race 2.0 | header credits the instructor |
| `turtle_race_2_0_with_betting.py` | Turtle Race 2.0 plus a betting mechanic | teacher-authored, extends `turtle_race_2_0.py` |
| `turtle_race_level_1.py` | Turtle Race, "Level 1" | teacher-authored, simplest version |
| `turtle_race_level_2.py` | Turtle Race, "Level 2" | teacher-authored, builds on Level 1 |
| `turtle_in_space.py` | Keyboard-controlled turtle "ship" (`onkey` bindings) | **references `space.jpg` and `rocketship.png`, which are not included — requires replacement images before it will run** |

`turtle_race_2_0*` and `turtle_race_level_*` are two apparently-independent Turtle Race lesson
families, both instructor-authored per their file headers; it's unclear whether they're two drafts
of the same lesson or separate tracks.

Additional near-duplicate Turtle Race and spirograph variants (from individual lesson sessions)
were not included here.
