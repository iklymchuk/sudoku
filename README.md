# Sudoku Game

A simple Sudoku game with a JavaScript frontend and Python Flask backend.

## Features

- Interactive Sudoku board
- Server-side validation of moves
- Visual feedback for valid/invalid moves
- Pre-filled starting grid

## How to Play

1. Click on any empty cell
2. Enter a number between 1-9
3. The server will validate your move and provide feedback
4. Green highlight indicates a valid move
5. Red highlight indicates an invalid move

## Technical Details

- Frontend: Vanilla JavaScript, HTML, and CSS
- Backend: Python Flask server
- No frameworks used as per requirements
- Server-side validation for all moves

## Build images
# Backend
```bash
cd backend
docker buildx build --platform linux/amd64 -t iklymchuk/sudoku-backend:latest --push .
```

# Frontend
```bash
cd frontend
docker buildx build --platform linux/amd64 -t iklymchuk/sudoku-frontend:latest --push .
```

## AWS
```bash
docker pull iklymchuk/sudoku-frontend:latest
docker pull iklymchuk/sudoku-backend:latest
docker-compose up -d
```

## Basic Backend Tests

```bash
python -m pytest --cov=app --cov-report=term-missing tests/                                          ─╯
=========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-7.4.3, pluggy-1.6.0
rootdir: /Users/iklymchuk/Projects/interview/sudoku/backend
configfile: pytest.ini
plugins: cov-4.1.0
collected 9 items                                                                                         

tests/test_config.py ....                                                                           [ 44%]
tests/test_game_service.py .                                                                        [ 55%]
tests/test_routes.py ..                                                                             [ 77%]
tests/test_validator.py ..                                                                          [100%]

---------- coverage: platform darwin, python 3.12.3-final-0 ----------
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
app/__init__.py                        2      0   100%
app/config.py                         11      0   100%
app/main.py                           15      3    80%   21-23
app/routes.py                         18      1    94%   19
app/services/__init__.py               2      0   100%
app/services/game_service.py          26      2    92%   33, 41
app/validators/__init__.py             2      0   100%
app/validators/move_validator.py      19      3    84%   22-23, 26
----------------------------------------------------------------
TOTAL                                 95      9    91%


============================================ 9 passed in 0.29s ============================================
```

## Resources

- Frontend image: https://hub.docker.com/repository/docker/iklymchuk/sudoku-frontend
- Backend image: https://hub.docker.com/repository/docker/iklymchuk/sudoku-backend
- AWS endpoint: http://ec2-54-191-78-71.us-west-2.compute.amazonaws.com/