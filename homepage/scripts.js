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
        // console.log(this);
        deleteRow(row.id);
        //this.deleteRow
      });
}

function deleteRow(rowId) {
    // row = t.parentNode.parentNode;
    // deleteRowButton = document.querySelectorAll('[id=deleteRow]').addEventListener('click', () => {
    row = document.querySelector(`table#table tr[id="${rowId}"]`);
    console.log(row);
    document.getElementById("table").deleteRow(row.rowIndex);
    // });
    // document.getElementById("table").deleteRow(row.rowIndex);
}
