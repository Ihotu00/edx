let board = {
    "1": "untouched1", "2": "untouched2", "3": "untouched3", "4": "untouched4", "5": "untouched5", "6": "untouched6", "7": "untouched7", "8": "untouched8", "9": "untouched9",
}

let playerX = true;

function ticTacToe(div) {
    document.getElementById(`${div}`).parentElement.classList.add('disable-div');
    if (playerX) {
        document.getElementById(`${div}`).innerHTML = 'X';
        board[div] = 'X';
        document.getElementById('next-tic-tac-toe-player').innerHTML = 'Player Two(O)';
    }
    else {
        document.getElementById(`${div}`).innerHTML = 'O';
        board[div] = 'O';
        document.getElementById('next-tic-tac-toe-player').innerHTML = 'Player One(X)';
    }
    if(currentPlayerWins()) {
        document.getElementById('board-container').classList.add('disable-div');
        document.getElementById('tic-tac-toe-retry').classList.remove('retry');
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
    if ((board['1'] === board['2'] && board['2'] === board['3']) ||
        (board['4'] == board['5'] && board['5'] == board['6']) ||
        (board['7'] == board['8'] && board['8'] == board['9']) ||
        (board['1'] == board['4'] && board['4'] == board['7']) ||
        (board['2'] == board['5'] && board['5'] == board['8']) ||
        (board['3'] == board['6'] && board['6'] == board['9']) ||
        (board['1'] == board['5'] && board['5'] == board['9']) ||
        (board['3'] == board['5'] && board['5'] == board['7'])
        ) { return true; }
}

function reset() {
    document.getElementById('tic-tac-toe-winner').innerHTML = '';
    document.getElementById('board-container').classList.remove('disable-div');
    document.getElementById('next-tic-tac-toe-player').innerHTML = 'Player One(X)';
    for (let i = 1; i < 9; i++) {
        var see = document.getElementById(`${i}`).parentElement.classList.remove('disable-div');
        document.getElementById(`${i}`).innerHTML = "";
        console.log(see);
      }
}
