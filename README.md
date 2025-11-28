# Sudoku Solver (Python, OOP, PEP 8)
> Author: **Soroosh Morshedi**  
> Website: [sorooshmorshedi.ir](https://sorooshmorshedi.ir)


A clean, object-oriented Sudoku solver written in Python, following PEP 8 naming conventions and best practices.

This project can:

- Parse multiple Sudoku puzzles from a text file.
- Solve each puzzle using a backtracking algorithm.
- Compute the 3-digit number formed by the first three digits of the first row of each solution.
- Sum those numbers across all solved puzzles.

---

## Features

- ✅ **Object-Oriented Design**  
  The core logic is encapsulated in a `Sudoku` class, responsible for representing and solving a single 9×9 grid.

- ✅ **PEP 8 Compliant & Readable**  
  Meaningful method and variable names, type hints, and docstrings are used throughout the code.

- ✅ **Backtracking Solver**  
  A classic, depth-first search backtracking algorithm is used to find valid solutions.

- ✅ **File-Based Batch Solving**  
  Multiple puzzles can be stored in a single `sudokus.txt` file and solved in one run.

- ✅ **Reusable as a Library**  
  You can import the `Sudoku` class and helpers into other projects or scripts.

---

## Project Structure

```text
.
├── sudoku.py      # Main solver module (Sudoku class + helpers + CLI entrypoint)
├── sudokus.txt    # Sample input file with multiple Sudoku puzzles
├── LICENSE        # MIT License
└── README.md      # Project documentation
```

---

## File Format: `sudokus.txt`

The solver expects puzzles in the following format:

- Each puzzle starts with a line beginning with `sdk`.
- Followed by **exactly 9 lines**, each containing 9 digits (`0–9`).
- `0` represents an empty cell.
- You may place multiple puzzles in the same file, one after another.

Example:

```text
sdk
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
sdk
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
```

---

## Installation

This project has no external dependencies beyond the Python standard library.

1. Make sure you have **Python 3.8+** installed.
2. Place the following files in the same directory:
   - `sudoku.py`
   - `sudokus.txt`
   - `LICENSE` (optional but recommended)
   - `README.md` (this file)

---

## Usage (Command Line)

From the directory containing `sudoku.py` and `sudokus.txt`, run:

```bash
python sudoku.py
```

### What happens:

- The script looks for `sudokus.txt` in the same directory as `sudoku.py`.
- It parses each puzzle defined in the file.
- For each puzzle:
  - Attempts to solve it.
  - Prints the solved grid in a human-friendly format (with box separators).
  - If the puzzle has no solution, a warning is printed and the puzzle is skipped.
- At the end:
  - It computes the sum of the 3-digit numbers formed by the first three digits of the first row of each solved puzzle.
  - Prints the final sum, for example:

```text
Total sum of first 3 digits of each solution: 728
```

---

## Usage as a Library

You can also import and use the solver inside your own Python code.

### Basic Example

```python
from pathlib import Path
from sudoku import Sudoku, parse_sudoku_file

# Parse all puzzles from file
for puzzle in parse_sudoku_file(Path("sudokus.txt")):
    if puzzle.solve():
        print("Solved puzzle:")
        print(puzzle)
        print()
    else:
        print("Puzzle has no solution.")
```

### Creating a Sudoku from In-Memory Lines

```python
from sudoku import Sudoku

lines = [
    "003020600",
    "900305001",
    "001806400",
    "008102900",
    "700000008",
    "006708200",
    "002609500",
    "800203009",
    "005010300",
]

sudoku = Sudoku.from_string_lines(lines)

if sudoku.solve():
    print("Solved:")
    print(sudoku)
else:
    print("No solution found.")
```

---

## Design Overview

### `Sudoku` Class

Core responsibilities:

- Store a 9×9 grid of integers (`0–9`).
- Provide helper methods:
  - `row_values(row_index)`
  - `column_values(column_index)`
  - `box_values(row_index, column_index)`
  - `candidates_for_cell(row_index, column_index)`
  - `find_next_empty()`
- Implement `solve()` using recursive backtracking.
- Implement `__str__()` for a readable grid representation:

Example output:

```text
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

---

## Extending the Project

Possible improvements and extensions:

- Add **heuristics** (e.g., MRV – Minimum Remaining Values) to speed up solving.
- Implement a separate `Solver` class with pluggable strategies.
- Add a CLI with arguments using `argparse` (e.g., custom input file paths).
- Add unit tests (e.g., using `pytest`) for the core logic.
- Add a simple GUI (e.g., Tkinter, PyQt, or a web frontend) for interactive solving.

---

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this code, including for commercial purposes, as long as the copyright
notice and permission notice are included in all copies or substantial portions of the Software.

See the [`LICENSE`](./LICENSE) file for full details.


---

## Author

``` js
 █████   ██   ██  █████    ██████   █████    ██   ██  ███████  ███████  ██   ██
██        ██ ██   ██  ██   ██       ██  ██   ███  ██    ███      ███    ██   ██
██         ███    █████    █████    █████    ██ █ ██    ███      ███    ███████
██          █     ██  ██   ██       ██ ██    ██  ███    ███      ███    ██   ██
██          █     ██  ██   ██       ██  ██   ██   ██    ███      ███    ██   ██
 █████      █     █████    ██████   ██   ██  ██   ██  ███████    ███    ██   ██

                    C Y B E R N I T H
                 
> ⚡ Crafted & unleashed by Soroosh morshedi ~ ( Cybernith ) ~
>  🌐  https://sorooshmorshedi.ir
> ❤️ Built with passion 
```



