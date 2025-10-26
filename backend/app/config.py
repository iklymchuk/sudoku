class Config:
    # Basic Configuration
    DEBUG = False
    TESTING = False
    
    # Application Configuration
    GRID_SIZE = 9
    
    # API Configuration
    API_PREFIX = '/api/v1'
    
    # Add more configuration as needed
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    
class ProductionConfig(Config):
    # Add production specific configuration
    pass