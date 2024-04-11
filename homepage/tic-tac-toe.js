let board = {
    "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "",
}

let playerX = true;

function ticTacToe(div) {
    document.getElementById(`${div}`).parentElement.classList.add('disable-div');
    playerX = !playerX;
    if (!playerX) {
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
        // console.log(currentPlayerWins());
        if (playerX) {
            document.getElementById('tic-tac-toe-winner').innerHTML = 'Player One (X) Wins!!!';
        }
        if (!playerX) {
            document.getElementById('tic-tac-toe-winner').innerHTML = 'Player Two (O) Wins!!!';
        }
    }
    console.log(playerX);
}

function currentPlayerWins() {
    // console.log(board['1']); console.log(board['2']); console.log(board['3']);
    // console.log(board);
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
