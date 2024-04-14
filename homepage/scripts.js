let todoDescription = {
    "0": "Beef, Carrots, Milk, Sausage, Noodles",
    "1": "@ 4:00pm"
};

let score = 0;
let number = Math.floor(Math.random() * 11);
let tries = 3;

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
    const table = document.querySelector('#table');
    var row = table.insertRow(-1);
    var cellCheck = row.insertCell(0);
    var cellTitle = row.insertCell(1);
    var cellButton = row.insertCell(2);
    row.id = table.tBodies[0].rows.length - 1;
    cellTitle.innerHTML = title;
    cellCheck.innerHTML = "<div class='form-check'><input class='form-check-input' type='checkbox' value='' name='check-1'></div>"
    cellButton.innerHTML = "<span class='material-icons'>delete</span>";
    cellButton.addEventListener('click', () => {
        deleteRow(row.id);
      });
    cellTitle.addEventListener('click', () => {
        var modalEl = new bootstrap.Modal(document.getElementById('view-description')).show();
        viewTodoDescription(row.id, cellTitle.innerHTML);
    });
    cellCheck.addEventListener('click', () => {
        strike(row.id);
      });
    todoDescription[row.id] = description;
    document.querySelector('#title').value = "";
    document.querySelector('#description').value = "";
}

function viewTodoDescription(rowId, title) {
    document.getElementById("description-body").innerHTML = todoDescription[rowId];
    document.getElementById("description-title").innerHTML = title;
}

function deleteRow(rowId) {
    var row = document.querySelector(`table#table tr[id="${rowId}"]`);
    document.getElementById("table").deleteRow(row.rowIndex);
    delete todoDescription[rowId];
}

function strike(rowId) {
    var row = document.querySelector(`table#table tr[id="${rowId}"]`);
    row.cells[1].classList.toggle('text-decoration-line-through');
}

function closeModal() {
    var myModalEl = document.getElementById('getInfo')
    myModalEl.addEventListener('hidden.bs.modal', function (event) {
        document.querySelector('#title').value = "";
        document.querySelector('#description').value = "";
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
        input.style.backgroundColor = '#ff0000';
        document.querySelector(response).innerHTML = "Hint: Use full name eg 'Naruto Uzumaki'";
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

function clickingGame() {
    score++;
    document.getElementById('score').innerHTML = score;
}

function guess() {
    console.log(number);
    var hint = document.getElementById('guess-hint');
    hint.innerHTML = "";
    var response = document.getElementById('guess-response');
    var guess = document.getElementById('guess');
    tries--
    if (tries == 0 && guess.value != number) {
        document.getElementById('answer').innerHTML = number
        document.getElementById('retry').classList.remove('retry');
        response.innerHTML = `You have run out of tries, the number was ${number}`;
        document.getElementById('guess-button').disabled = true;
        guess.disabled = true;
        document.getElementById('guess-hint').innerHTML = "";
    }
    else {
        if (guess.value == number) {
            document.getElementById('answer').innerHTML = number
            response.innerHTML = "Correct!!!";
            response.style.color = "#00ff00";
            guess.disabled = true;
            document.getElementById('guess-button').disabled = true;
            document.getElementById('retry').classList.remove('retry');
        }
        else {
            response.innerHTML = `Wrong!!! You have ${tries} tries left`;
            response.style.color = "#ff0000";
            if(guess.value > number) { hint.innerHTML = "Your guess is too high"}
            if(guess.value < number) { hint.innerHTML = "Your guess is too low"}
        }
    }
}

function retry() {
    document.getElementById('answer').innerHTML = "???"
    document.getElementById('retry').classList.add('retry');
    number = Math.floor(Math.random() * 11);
    tries = 3;
    document.getElementById('guess-button').disabled = false;
    document.getElementById('guess').disabled = false;
    document.getElementById('guess').value = "";
    var response = document.getElementById('guess-response').innerHTML = "";
    document.getElementById('guess-hint').innerHTML = "";
}
