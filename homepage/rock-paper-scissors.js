let moves = {
    "player1": "",
    "player2": ""
}

let turn = "player1";

function play(move) {
    var turnTtext = document.getElementById('turn-text').innerHTML;
    if (turn == "player1") {
        moves.player1 = move;
        turn = "player2";
        turnText = "Second Player's Move";
    }

    if (turn == "player2") {
        moves.player2 = move;
        turnText = "Click the submit button to see the winner";
        document.getElementById('rock-paper-scissors-button').disabled= false;
    }
    console.log(moves)
}
