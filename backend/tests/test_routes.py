import pytest
from app.main import create_app
from app.config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_grid(client):
    response = client.get('/api/v1/grid')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 9
    assert len(response.json[0]) == 9

def test_validate_move(client):
    test_data = {
        'row': 0,
        'col': 0,
        'number': 5
    }
    response = client.post('/api/v1/validate', json=test_data)
    assert response.status_code == 200
    assert 'valid' in response.json