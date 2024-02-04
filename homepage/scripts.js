function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}

function addRow() {
    const first = document.querySelector('#first').value;
    const last = document.querySelector('#last').value;
    const handle = document.querySelector('#handle').value;
    const table = document.querySelector('#table');
    var rowId = table.tBodies[0].rows.length;
    var row = table.insertRow(-1);
    var cellFirst = row.insertCell(0);
    var cellLast = row.insertCell(1);
    var cellHandle = row.insertCell(2);
    var cellButton = row.insertCell(3);
    cellFirst.innerHTML = first;
    cellLast.innerHTML = last;
    cellHandle.innerHTML = handle;
    cellButton.innerHTML = "<button class='btn-primary' id=$`{rowId}`>Delete</button>";
    cellButton.addEventListener('click', () => {
        deleteRow(rowId);
      });
}

function deleteRow(rowIndex) {
    document.getElementById("table").deleteRow(rowIndex)
}
