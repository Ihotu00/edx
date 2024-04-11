let moves = {
    "player1": "",
    "player2": ""
}

let turn = "player1";

function play(move) {
    if (turn == "player1") {
        moves.player1 = move;
        document.getElementById('turn-text').innerHTML = "Second Player's Move";
    }

    if (turn == "player2") {
        moves.player2 = move;
        document.getElementById('turn-text').innerHTML = "Click the submit button to see the winner";
        document.getElementById('rock-paper-scissors-button').disabled= false;
        document.getElementById('rock').classList.add('disable-div');
        document.getElementById('paper').classList.add('disable-div');
        document.getElementById('scissors').classList.add('disable-div');
    }
    turn = "player2";
    console.log(moves);
}
