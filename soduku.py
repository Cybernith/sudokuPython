from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Set, Tuple

Grid = List[List[int]]


@dataclass
class Sudoku:
    grid: Grid

    SIZE: int = 9
    BOX_SIZE: int = 3

    @classmethod
    def from_string_lines(cls, lines: Iterable[str]) -> "Sudoku":
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        if len(cleaned_lines) != cls.SIZE:
            raise ValueError("Sudoku must have exactly 9 non-empty lines.")

        grid: Grid = [
            [int(char) for char in line]
            for line in cleaned_lines
        ]
        if any(len(row) != cls.SIZE for row in grid):
            raise ValueError("Each Sudoku row must contain exactly 9 digits.")

        return cls(grid)

    def row_values(self, row_index: int) -> List[int]:
        return self.grid[row_index]

    def column_values(self, column_index: int) -> List[int]:
        return [self.grid[row_index][column_index] for row_index in range(self.SIZE)]

    def box_values(self, row_index: int, column_index: int) -> List[int]:
        box_row_start = (row_index // self.BOX_SIZE) * self.BOX_SIZE
        box_column_start = (column_index // self.BOX_SIZE) * self.BOX_SIZE

        return [
            self.grid[r][c]
            for r in range(box_row_start, box_row_start + self.BOX_SIZE)
            for c in range(box_column_start, box_column_start + self.BOX_SIZE)
        ]

    def candidates_for_cell(self, row_index: int, column_index: int) -> Set[int]:
        if self.grid[row_index][column_index] != 0:
            return set()

        used_values = set(
            self.row_values(row_index)
            + self.column_values(column_index)
            + self.box_values(row_index, column_index)
        )

        return {value for value in range(1, 10) if value not in used_values}

    def find_next_empty(self) -> Optional[Tuple[int, int]]:
        for row_index in range(self.SIZE):
            for column_index in range(self.SIZE):
                if self.grid[row_index][column_index] == 0:
                    return row_index, column_index
        return None

    def solve(self) -> bool:
        empty_cell = self.find_next_empty()
        if empty_cell is None:
            return True  

        row_index, column_index = empty_cell
        for candidate in sorted(self.candidates_for_cell(row_index, column_index)):
            self.grid[row_index][column_index] = candidate
            if self.solve():
                return True
            self.grid[row_index][column_index] = 0

        return False

    def __str__(self) -> str:
        lines: List[str] = []
        for row_index, row in enumerate(self.grid):
            if row_index and row_index % self.BOX_SIZE == 0:
                lines.append("-" * 21)

            row_chunks: List[str] = []
            for column_index, value in enumerate(row):
                if column_index and column_index % self.BOX_SIZE == 0:
                    row_chunks.append("|")
                row_chunks.append(str(value) if value != 0 else ".")
            lines.append(" ".join(row_chunks))
        return "\n".join(lines)


def parse_sudoku_file(path: Path) -> Iterable[Sudoku]:
    lines_buffer: List[str] = []

    with path.open("r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue

            if line.startswith("sdk"):
                if lines_buffer:
                    yield Sudoku.from_string_lines(lines_buffer)
                    lines_buffer = []
                continue

            lines_buffer.append(line)

            if len(lines_buffer) == 9:
                yield Sudoku.from_string_lines(lines_buffer)
                lines_buffer = []

    if lines_buffer:
        yield Sudoku.from_string_lines(lines_buffer)


def sum_of_first_three_digits(sudoku: Sudoku) -> int:
    first_row = sudoku.grid[0]
    a, b, c = first_row[:3]
    return a * 100 + b * 10 + c


def solve_all_from_file(path: Path) -> int:
    total_sum = 0

    for index, puzzle in enumerate(parse_sudoku_file(path), start=1):
        print(f"Solving Sudoku #{index}...")
        if not puzzle.solve():
            print(f"Sudoku #{index} has no solution. Skipping.")
            continue

        print(puzzle)
        print("=" * 40)

        total_sum += sum_of_first_three_digits(puzzle)

    return total_sum


def main() -> None:
    base_directory = Path(__file__).resolve().parent
    sudoku_file = base_directory / "sudokus.txt"

    if not sudoku_file.exists():
        raise FileNotFoundError(
            f"Could not find 'sudokus.txt' next to {__file__!r}. "
            "Make sure the file exists and try again."
        )

    total_sum = solve_all_from_file(sudoku_file)
    print(f"Total sum of first 3 digits of each solution: {total_sum}")


if __name__ == "__main__":
    main()
