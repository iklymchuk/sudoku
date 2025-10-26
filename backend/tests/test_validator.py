"""Test input validation logic."""
import pytest
from app.validators.move_validator import MoveValidator

@pytest.fixture
def validator():
    return MoveValidator()

def test_validate_input_types():
    """Test validation of input types."""
    validator = MoveValidator()
    
    # Valid input
    assert validator.validate_input(0, 0, 1) is True
    
    # Invalid row type
    assert validator.validate_input("0", 0, 1) is False
    
    # Invalid column type
    assert validator.validate_input(0, "0", 1) is False
    
    # Invalid number type
    assert validator.validate_input(0, 0, "1") is False

def test_validate_input_ranges():
    """Test validation of input ranges."""
    validator = MoveValidator()
    
    # Valid input
    assert validator.validate_input(0, 0, 1) is True
    
    # Invalid row (negative)
    assert validator.validate_input(-1, 0, 1) is False
    
    # Invalid row (too large)
    assert validator.validate_input(9, 0, 1) is False
    
    # Invalid column (negative)
    assert validator.validate_input(0, -1, 1) is False
    
    # Invalid column (too large)
    assert validator.validate_input(0, 9, 1) is False
    
    # Invalid number (too small)
    assert validator.validate_input(0, 0, 0) is False
    
    # Invalid number (too large)
    assert validator.validate_input(0, 0, 10) is False