function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}
var tableContent = [{first: "Ihotu", last: "Ifenne", handle: "@ii"},
                    {first: "John", last: "Doe", handle:"@jd"}]

function addRow() {
    console.log("started")
    const first = document.querySelector('#first').value;
    const last = document.querySelector('#last').value;
    const handle = document.querySelector('#handle').value;
    const table = document.querySelector('#table');
    console.log(first, last, handle)
    var row = document.createElement('tr');
    var cellFirst = document.createElement('td');
    var textFirst = document.createTextNode(first);
    var cellLast = document.createElement('td');
    var textLast = document.createTextNode(last);
    var cellHandle = document.createElement('td');
    var textHandle = document.createTextNode(handle);
    cellFirst.appendChild(textFirst);
    row.appendChild(cellFirst);
    cellLast.appendChild(textLast);
    row.appendChild(cellLast);
    cellHandle.appendChild(textHandle);
    row.appendChild(cellHandle);
    table.appendChild(row);
}
