function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}
var tableContent = [{first: "Ihotu", last: "Ifenne", handle: "@ii"},
                    {first: "John", last: "Doe", handle:"@jd"}]

function addRow() {
    const first = document.querySelector('#first').value;
    const last = document.querySelector('#last').value;
    const handle = document.querySelector('#handle').value;
    const table = document.querySelector('#table');
    var row = table.insertRow(-1);
    var cellFirst = row.insertCell(0);
    var cellLast = row.insertCell(1);
    var cellHandle = row.insertCell(2);
    cellFirst.innerHTML = first;
    cellLast.innerHTML = last;
    cellHandle.innerHTML = handle;
    // var row = document.createElement('tr');
    // var cellFirst = document.createElement('td');
    // var textFirst = document.createTextNode(first);
    // var cellLast = document.createElement('td');
    // var textLast = document.createTextNode(last);
    // var cellHandle = document.createElement('td');
    // var textHandle = document.createTextNode(handle);
    // cellFirst.appendChild(textFirst);
    // row.appendChild(cellFirst);
    // cellLast.appendChild(textLast);
    // row.appendChild(cellLast);
    // cellHandle.appendChild(textHandle);
    // row.appendChild(cellHandle);
    // table.appendChild(row);
}
