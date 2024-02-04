function navigate(page) {
    var content = document.querySelector('#content');
    content.src = page;
}
var tableContent = [{first: "Ihotu", last: "Ifenne", handle: "@ii"},
                    {first: "John", last: "Doe", handle:"@jd"}]

function addRow() {
    const first = document.getElementById('first');
    const last = document.getElementById('last');
    const handle = document.getElementById('handle');
    const table = document.getElementById('#table');
    var row = document.createElement('tr');
    var cell = document.createElement('td');
    var text = document.createTextNode(first);
    var cell = document.createElement('td');
    var text = document.createTextNode(first);
    var cell = document.createElement('td');
    var text = document.createTextNode(first);
}
