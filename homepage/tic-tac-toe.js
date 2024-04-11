let board = {
    "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "",
}

let playerX = true;

function ticTacToe(div) {
    if (playerX) {
        document.getElementById(`${div}`).innerHTML = 'X';
        board[div] = 'X';
        document.getElementById('current-tic-tac-toe-player').innerHTML = 'Player Two(O)';
    }
    else {
        document.getElementById(`${div}`).innerHTML = 'O';
        board[div] = 'O';
        document.getElementById('current-tic-tac-toe-player').innerHTML = 'Player One(X)';
    }
    document.getElementById(`${div}`).parentElement.classList.add('disable-div');
    if(currentPlayerWins()) {
        console.log(currentPlayerWins());
        console.log(board);
        if (playerX) {
            document.getElementById('tic-tac-toe-winner').innerHTML = 'Player One (X) Wins!!!';
        }
        if (!playerX) {
            document.getElementById('tic-tac-toe-winner').innerHTML = 'Player Two (O) Wins!!!';
        }
    }
    else { playerX = !playerX; }
}

function currentPlayerWins() {
    if (
        (board['1'] == board['2'] && board['2'] == board['3'])
        // (board['4'] == board['5'] && board['5'] == board['6']) ||
        // (board['7'] == board['8'] && board['8'] == board['9']) ||
        // (board['1'] == board['4'] && board['4'] == board['7']) ||
        // (board['2'] == board['5'] && board['5'] == board['8']) ||
        // (board['3'] == board['6'] && board['6'] == board['9']) ||
        // (board['1'] == board['5'] && board['5'] == board['9']) ||
        // (board['3'] == board['5'] && board['5'] == board['7'])
        ) { return true; }
}
