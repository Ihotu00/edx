document.addEventListener('DOMContentLoaded', function() {
    selected_tab(){
        console.log(tab)
        if (tab == 'home') {
            document.getElementById('home-tab').classList.add("active");
            document.getElementById('home-tab-pane').classList.add("show active");
        }

        if (tab == 'groups') {
            document.getElementById('groups-tab').classList.add("active");
            document.getElementById('groups-tab-pane').classList.add("show active");
        }
    }
});

function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}


function selected(group) {
    console.log(group)
    document.getElementById('group_header').innerHTML = group["group_name"];
    document.getElementById('group_id').value = group["group_id"];
    document.getElementById('tab').value = "groups";
}
