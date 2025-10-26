"""Test the Sudoku grid validation logic."""
import pytest
from app.services.game_service import GameService

@pytest.fixture
def game_service():
    return GameService()

def test_is_valid_move():
    """Test if move validation works correctly."""
    game_service = GameService()
    
    # Test valid move
    assert game_service.is_valid_move([[0] * 9 for _ in range(9)], 0, 0, 1) is True
    
    # Test row conflict
    grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
    assert game_service.is_valid_move(grid, 0, 1, 1) is False
    
    # Test column conflict
    grid = [[1] + [0] * 8 for _ in range(9)]
    assert game_service.is_valid_move(grid, 1, 0, 1) is False
    
    # Test box conflict
    grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert game_service.is_valid_move(grid, 0, 1, 1) is False