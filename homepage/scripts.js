function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}

function addRow() {
    const first = document.querySelector('#first').value;
    const last = document.querySelector('#last').value;
    const handle = document.querySelector('#handle').value;
    const table = document.querySelector('#table');
    var row = table.insertRow(-1);
    var cellFirst = row.insertCell(0);
    var cellLast = row.insertCell(1);
    var cellHandle = row.insertCell(2);
    var cellButton = row.insertCell(3);
    row.id = table.tBodies[0].rows.length - 1;
    cellFirst.innerHTML = first;
    cellLast.innerHTML = last;
    cellHandle.innerHTML = handle;
    cellButton.innerHTML = "<button class='btn'>Delete</button>";
    cellButton.addEventListener('click', () => {
        deleteRow(row.id);
      });
    document.querySelector('#first').value = "";
    document.querySelector('#last').value = "";
    document.querySelector('#handle').value = "";
}

function deleteRow(rowId) {
    var row = document.querySelector(`table#table tr[id="${rowId}"]`);
    document.getElementById("table").deleteRow(row.rowIndex);
}

function closeModal() {
    var myModalEl = document.getElementById('getInfo')
    myModalEl.addEventListener('hidden.bs.modal', function (event) {
        document.querySelector('#first').value = "";
        document.querySelector('#last').value = "";
        document.querySelector('#handle').value = "";
    })
}

function checkTrivia(answer, response) {
    document.querySelector(response).innerHTML = "";
    let input = document.querySelector(`#${answer}`);
    if ((answer == 'minato' && input.value.localeCompare('Minato Namikaze', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'kushina' && input.value.localeCompare('Kushina Uzumaki', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'konoha' && input.value.localeCompare('Konohagakure', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'kurama' && input.value.localeCompare('Kurama', 'en', {sensitivity: 'base'}) == 0)) {
        input.style.backgroundColor = '#00ff00';
    }
    else {
        input.style.backgroundColor = '#ff3300';
        document.querySelector(response).innerHTML = "Hint: Use full name ed 'Naruto Uzumaki'";
    }
}

function submitTrivia() {
    input1 = document.querySelector('#minato').value;
    input2 = document.querySelector('#kushina').value;
    input3 = document.querySelector('#konoha').value;
    input4 = document.querySelector('#kurama').value;
    if ((input1.localeCompare('Minato Namikaze', 'en', {sensitivity: 'base'}) == 0) &&
        (input2.localeCompare('Kushina Uzumaki', 'en', {sensitivity: 'base'}) == 0) &&
        (input3.localeCompare('Konohagakure', 'en', {sensitivity: 'base'}) == 0) &&
        (input4.localeCompare('Kurama', 'en', {sensitivity: 'base'}) == 0)) {
            document.querySelector('#trivia-card').style.backgroundColor = '#00ff00';
            console.log('correct');
        }
    else { document.querySelector('#trivia-card').style.backgroundColor = '#ff3300'; console.log('wrong'); }
}


// function validateTrivia(answer, input) {
//     if ((answer == 'minato' && input.localeCompare('Minato Namikaze', 'en', {sensitivity: 'base'}) == 0) ||
//         (answer == 'kushina' && input.localeCompare('Kushina Uzumaki', 'en', {sensitivity: 'base'}) == 0) ||
//         (answer == 'konoha' && input.localeCompare('Konohagakure', 'en', {sensitivity: 'base'}) == 0) ||
//         (answer == 'kurama' && input.localeCompare('Kurama', 'en', {sensitivity: 'base'}) == 0)) {
//             return true;
//         }
//     else { return false;}
// }
