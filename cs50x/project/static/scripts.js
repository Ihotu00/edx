function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}


function selected(group) {
    console.log(group["group_name"]);
    document.getElementById('group_header').innerHTML = group["group_name"];
}
