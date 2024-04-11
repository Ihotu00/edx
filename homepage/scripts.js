let todoDescription = {
    "0": "Beef, Carrots, Milk, Sausage, Noodles",
    "1": "@ 4:00pm"
};

console.log(todoDescription);

function navigate(page) {
    var content = document.querySelector('#content');
    var previousPage = content.src.split('/')[3].split('.')[0];
    document.querySelector(`#${previousPage}`).classList.remove('active')
    document.querySelector(`#${page}`).classList.add('active')
    content.src = `${page}.html`;
}

function addRow() {
    const title = document.querySelector('#title').value;
    const description = document.querySelector('#description').value;
    // const handle = document.querySelector('#handle').value;
    const table = document.querySelector('#table');
    var row = table.insertRow(-1);
    var cellTitle = row.insertCell(1);
    // var cellDescription = row.insertCell(1);
    // var cellHandle = row.insertCell(2);
    var cellButton = row.insertCell(2);
    row.id = table.tBodies[0].rows.length - 1;
    cellTitle.innerHTML = title;
    // cellDescription.innerHTML = description;
    // cellHandle.innerHTML = handle;
    cellButton.innerHTML = "<span class='material-icons'>delete</span>";
    cellButton.addEventListener('click', () => {
        deleteRow(row.id);
      });
    document.querySelector('#title').value = "";
    document.querySelector('#description').value = "";
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
        console.log(test);
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
        }
    else { document.querySelector('#trivia-card').style.backgroundColor = '#ff0000'; }
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
