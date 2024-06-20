let moves = {
    "player1": "",
    "player2": ""
}

let turn = "player1";

function play(move) {
    if (turn == "player1") {
        moves.player1 = move;
        document.getElementById('currentPlayer').innerHTML = "Player Two";
        document.getElementById('turn-text').innerHTML = "Second Player's Move";
    }

    if (turn == "player2") {
        moves.player2 = move;
        document.getElementById('currentPlayer').innerHTML = "";
        document.getElementById('turn-text').innerHTML = "Click the submit button to see the winner";
        document.getElementById('rock-paper-scissors-button').disabled= false;
        document.getElementById('rock').classList.add('disable-div');
        document.getElementById('paper').classList.add('disable-div');
        document.getElementById('scissors').classList.add('disable-div');
    }
    turn = "player2";
}

function replay() {
    moves.player1 = "";
    moves.player2 = "";
    turn = "player1";
    document.getElementById('currentPlayer').innerHTML = "Player One";
    document.getElementById('turn-text').innerHTML = "First Player's Move";
    document.getElementById('rock-paper-scissors-button').disabled= true;
    document.getElementById('rock').classList.remove('disable-div');
    document.getElementById('paper').classList.remove('disable-div');
    document.getElementById('scissors').classList.remove('disable-div');
    document.getElementById('rock-paper-scissors-retry').classList.add('retry');
    document.getElementById('scissors-wins').classList.add('retry');
    document.getElementById('paper-wins').classList.add('retry');
    document.getElementById('rock-wins').classList.add('retry');
    document.getElementById('winner').innerHTML = "";
}

function submitRockPaperScisssors() {
    if (getWinner(moves.player1, moves.player2) == 1) {
        document.getElementById('winner').innerHTML = "Player One Wins!!";
        document.getElementById(`${moves.player1}-wins`).classList.remove('retry');
    }
    if (getWinner(moves.player1, moves.player2) == 2) {
        document.getElementById('winner').innerHTML = "Player Two Wins!!";
        document.getElementById(`${moves.player2}-wins`).classList.remove('retry');
    }
    document.getElementById('rock-paper-scissors-retry').classList.remove('retry');
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
