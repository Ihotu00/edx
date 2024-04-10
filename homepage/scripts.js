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
    // if (answer.localeCompare(input.value, 'en', { sensitivity: 'base' }) == 0) {
    if(validateTrivia(answer, input.value)){
        input.style.backgroundColor = '#00ff00';
    }
    else {
        input.style.backgroundColor = '#ff3300';
        document.querySelector(response).innerHTML = "Hint: Use full name";
    }
}

function validateTrivia(answer, input) {
    console.log(input)
    if ((answer == 'minato' && input.localCompare('Minato Namikaze', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'kushina' && input.localCompare('Kushina Uzumaki', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'konoha' && input.localCompare('Konohagakure', 'en', {sensitivity: 'base'}) == 0) ||
        (answer == 'kurama' && input.localCompare('Kurama', 'en', {sensitivity: 'base'}) == 0)) {
            return true;
        }
    else { return false;}
}
