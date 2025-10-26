"""Input validation for moves"""
class MoveValidator:
    def __init__(self):
        self.grid_size = 9

    def validate_input(self, row, col, num):
        # Type checks
        if not all(isinstance(x, int) for x in [row, col, num]):
            return False

        # Range checks
        if not (0 <= row < self.grid_size and 0 <= col < self.grid_size and 1 <= num <= 9):
            return False

        return True

    def validate_move(self, data):
        try:
            row = data.get('row')
            col = data.get('col')
            num = data.get('number')
        except Exception:
            return {"valid": False, "error": "Invalid payload"}

        if not self.validate_input(row, col, num):
            return {"valid": False, "error": "Invalid input"}

        return {"valid": True}
