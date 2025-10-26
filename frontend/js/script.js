document.addEventListener('DOMContentLoaded', initGame);

let board = [];
const messageElement = document.getElementById('message');
const API_BASE_URL = 'http://{backend_host}:8900/api/v1';

async function initGame() {
    try {
        const response = await fetch(`${API_BASE_URL}/grid`);
        board = await response.json();
        renderBoard();
    } catch (error) {
        showMessage('Error loading the game', 'error');
    }
}

function renderBoard() {
    const boardElement = document.getElementById('board');
    boardElement.innerHTML = '';

    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (board[row][col] !== 0) {
                cell.textContent = board[row][col];
                cell.classList.add('fixed');
            } else {
                cell.addEventListener('click', () => handleCellClick(cell, row, col));
            }
            boardElement.appendChild(cell);
        }
    }
}

function handleCellClick(cell, row, col) {
    const number = prompt('Enter a number (1-9):', '');
    if (!number) return;

    const num = parseInt(number);
    if (isNaN(num) || num < 1 || num > 9) {
        showMessage('Please enter a valid number between 1 and 9', 'error');
        return;
    }

    validateMove(row, col, num, cell);
}

async function validateMove(row, col, number, cell) {
    try {
        const response = await fetch(`${API_BASE_URL}/validate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ row, col, number })
        });

        const result = await response.json();
        
        if (result.valid) {
            cell.textContent = number;
            cell.classList.remove('invalid');
            cell.classList.add('valid');
            board[row][col] = number;
            showMessage('Valid move!', 'success');
        } else {
            cell.classList.remove('valid');
            cell.classList.add('invalid');
            showMessage(result.error || 'Invalid move!', 'error');
        }

        // Remove the visual feedback after 1 second
        setTimeout(() => {
            cell.classList.remove('valid', 'invalid');
        }, 1000);

    } catch (error) {
        showMessage('Error validating move', 'error');
    }
}

function showMessage(text, type) {
    messageElement.textContent = text;
    messageElement.className = `message ${type}`;
}