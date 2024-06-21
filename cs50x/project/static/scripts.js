// document.addEventListener('DOMContentLoaded', function() {
//     if (tab == 'home') {
//         document.getElementById('groups-tab').classList.remove("active");
//         document.getElementById('groups-tab-pane').classList.remove("show");
//         document.getElementById('groups-tab-pane').classList.remove("active");
//         document.getElementById('profile-tab').classList.remove("active");
//         document.getElementById('profile-tab-pane').classList.remove("show");
//         document.getElementById('profile-tab-pane').classList.remove("active");
//         document.getElementById('home-tab').classList.add("active");
//         document.getElementById('home-tab-pane').classList.add("show");
//         document.getElementById('home-tab-pane').classList.add("active");
//     }

//     if (tab == 'groups') {
//         document.getElementById('home-tab').classList.remove("active");
//         document.getElementById('home-tab-pane').classList.remove("show");
//         document.getElementById('home-tab-pane').classList.remove("active");
//         document.getElementById('profile-tab').classList.remove("active");
//         document.getElementById('profile-tab-pane').classList.remove("show");
//         document.getElementById('profile-tab-pane').classList.remove("active");
//         document.getElementById('groups-tab').classList.add("active");
//         document.getElementById('groups-tab-pane').classList.add("show");
//         document.getElementById('groups-tab-pane').classList.add("active");
//     }

//     if (tab == 'profile') {
//         document.getElementById('home-tab').classList.remove("active");
//         document.getElementById('home-tab-pane').classList.remove("show");
//         document.getElementById('home-tab-pane').classList.remove("active");
//         document.getElementById('groups-tab').classList.remove("active");
//         document.getElementById('groups-tab-pane').classList.remove("show");
//         document.getElementById('groups-tab-pane').classList.remove("active");
//         document.getElementById('profile-tab').classList.add("active");
//         document.getElementById('profile-tab-pane').classList.add("show");
//         document.getElementById('profile-tab-pane').classList.add("active");
//     }
// });

function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}

function show_modal(id) {
    new bootstrap.Modal(document.getElementById(id)).show();
}

function hide_modal(id) {
    new bootstrap.Modal(document.getElementById(id)).hide();
}


function selected(group) {
    document.getElementById('group_header').innerHTML = group["group_name"];
    document.getElementById('group_id').value = group["group_id"];
    document.getElementById('tab').value = "groups";
}


function send_post() {
    $.ajax({
        url: '/post',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'group_id': document.getElementById('group_id').value,
            'message': document.getElementById('post').value }),
        success: function(response) {
            console.log(`success: ${JSON.stringify(response)}`);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function create_group() {
    modal = new bootstrap.Modal(document.getElementById('add-group-modal'));

    $.ajax({
        url: '/create/group',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'group_name': document.getElementById('group_name').value}),
        success: function(response) {
            hide_modal('add-group-modal');
            console.log(`success: ${JSON.stringify(response)}`);
            selected(response)
        },
        error: function(error) {
            console.log(error.responseText);
            show("group-taken")
        }
    });
}
