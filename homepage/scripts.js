function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}
var tableContent = [{first: "Ihotu", last: "Ifenne", handle: "@ii"},
                    {first: "John", last: "Doe", handle:"@jd"}]

function addRow() {
    // console.log("started")
    const first = document.getElementById('#first').value;
    const last = document.getElementById('#last').value;
    const handle = document.getElementById('#handle').value;
    const table = document.getElementById('#table');
    console.log(first)
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
