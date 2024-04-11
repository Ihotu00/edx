let moves = {
    "player1": "",
    "player2": ""
}

let playerX = true;

function ticTacToe(div) {
    if (playerX) {
        document.getElementById(`${div}`).innerHTML = 'X';
    }
    else {
        document.getElementById(`${div}`).innerHTML = 'O';
    }
    document.getElementById(`${div}`).parentElement.classList.add('disable-div');
    playerX = !playerX;
}
