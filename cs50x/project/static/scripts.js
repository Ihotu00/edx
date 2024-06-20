document.addEventListener('DOMContentLoaded', function(tab) {
    if (tab === 'posts') {
        answer.style.backgroundColor = 'green';
        document.querySelector('#response2').innerHTML = 'Correct';
    }
});

function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}


function selected(group) {
    document.getElementById('group_header').innerHTML = group["group_name"];
    document.getElementById('group_id').value = group["group_id"];
    document.getElementById('tab').value = "groups";
}
