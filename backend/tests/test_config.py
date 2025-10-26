"""Test configuration handling."""
from app.config import Config, DevelopmentConfig, TestingConfig, ProductionConfig

def test_base_config():
    """Test base configuration settings."""
    config = Config()
    assert config.DEBUG is False
    assert config.TESTING is False
    assert config.GRID_SIZE == 9
    assert config.API_PREFIX == '/api/v1'

def test_development_config():
    """Test development configuration settings."""
    config = DevelopmentConfig()
    assert config.DEBUG is True
    assert config.TESTING is False

def test_testing_config():
    """Test testing configuration settings."""
    config = TestingConfig()
    assert config.TESTING is True

def test_production_config():
    """Test production configuration settings."""
    config = ProductionConfig()
    assert config.DEBUG is False
    assert config.TESTING is False