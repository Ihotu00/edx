let board = {
    "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "",
}

let playerX = true;

function ticTacToe(div) {
    if (playerX) {
        document.getElementById(`${div}`).innerHTML = 'X';
        board[div] = 'X';
    }
    else {
        document.getElementById(`${div}`).innerHTML = 'O';
        board[div] = 'O';
    }
    document.getElementById(`${div}`).parentElement.classList.add('disable-div');
    getTicTacToeWinner();
    playerX = !playerX;
}

function getTicTacToeWinner() {
    if ((board['1'] == board['2'] && board['2'] == board['3']) ||
        (board['4'] == board['5'] && board['5'] == board['6']) ||
        (board['7'] == board['8'] && board['8'] == board['9']) ||
        (board['1'] == board['4'] && board['4'] == board['7']) ||
        (board['2'] == board['5'] && board['5'] == board['8']) ||
        (board['3'] == board['6'] && board['6'] == board['9']) ||
        (board['1'] == board['5'] && board['5'] == board['9']) ||
        (board['3'] == board['5'] && board['5'] == board['7']) ||
        ) {  }
}
