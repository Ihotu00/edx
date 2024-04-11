// let moves = {
//     "player1": "",
//     "player2": ""
// }

let playerX = true;

function ticTacToe(div) {
    console.log(div);
    if (playerX) {
        document.getElementById(`${div}`).innerHTML = 'X';
    }
    else {
        document.getElementById(`${div}`).innerHTML = 'O';
    }
    document.getElementById(`${div}`).classList.add('disable-div');
    playerX = !playerX;
    console.log(playerX);
}
