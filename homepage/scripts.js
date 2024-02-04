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
    cellFirst.innerHTML = first;
    cellLast.innerHTML = last;
    cellHandle.innerHTML = handle;
    cellButton.innerHTML = "<button class='btn-primary'>Delete</button>";
    // cellButton = document.createElement("BUTTON");
    // cellButton.textContent = "Delete";
}

function deleteRow() {
    newButton.addEventListener('click', () => {
        alert('New button clicked!');
      });
    document.getElementById("table").deleteRow(rowIndex)
}
