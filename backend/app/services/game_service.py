"""Game service: business logic for Sudoku"""
from copy import deepcopy

# Mock Sudoku grid (9x9)
MOCK_GRID = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


class GameService:
    def __init__(self):
        # In a real app this could be a DB or cache; here we use an in-memory mock
        self._grid = deepcopy(MOCK_GRID)

    def get_grid(self):
        return deepcopy(self._grid)

    def is_valid_move(self, grid, row, col, num):
        # Check row
        if num in grid[row]:
            return False

        # Check column
        if num in [grid[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if grid[i][j] == num:
                    return False

        return True

    def validate_move(self, row, col, num):
        current_grid = deepcopy(self._grid)
        # Temporarily remove any value at position for validation
        current_grid[row][col] = 0
        valid = self.is_valid_move(current_grid, row, col, num)
        if valid:
            # Apply move
            self._grid[row][col] = num
        return {"valid": valid}
