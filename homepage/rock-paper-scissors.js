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
        document.getElementById('rock-paper-scissors-retry').classList.remove('retry');
    }
    turn = "player2";
}

function replay() {
    moves.player1 = "";
    moves.player2 = "";
    turn = "player1";
    document.getElementById('turn-text').innerHTML = "First Player's Move";
    document.getElementById('rock-paper-scissors-button').disabled= true;
    document.getElementById('rock').classList.remove('disable-div');
    document.getElementById('paper').classList.remove('disable-div');
    document.getElementById('scissors').classList.remove('disable-div');
    document.getElementById('rock-paper-scissors-retry').classList.add('retry');
}

function submitRockPaperScisssors() {

}

function getWinner(move1, move2) {
    if (move1 == 'rock') {
        if (move2 == 'paper') { return 2; }
        if (move2 == 'scissors') { return 1; }
    }

    if (move1 == 'paper') {
        if(move2 == 'rock') { return 1; }
        if(move2 == 'scissors') { return 2; }
    }

    if (move1 == 'scissors') {
        if(move2 == 'rock') { return 2; }
        if(move2 == 'paper') { return 1; }
    }
}
