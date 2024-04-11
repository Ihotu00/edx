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
    playerX = !playerX;
}
