let moves = {
    "player1": "",
    "player2": ""
}

let turn = "player1";

function play(move) {
    if (turn == "player1") {
        moves.player1 = move;
        turn = "player2";
    }

    if (turn == "player2") {
        moves.player2 = move;
    }
}
