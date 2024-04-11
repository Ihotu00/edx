let moves = {
    "player1": "",
    "player2": ""
}

let turn = "player-x";

function ticTacToe(div) {
    if (turn == "player-x") {
        document.getElementById(`${div}`).innerHTML = 'X'
    }
    if (turn == "player-y") {
        document.getElementById(`${div}`).innerHTML = 'X'
    }
}
