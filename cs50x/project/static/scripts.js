var group_modal = new bootstrap.Modal(document.getElementById('add-group-modal'));

function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}

function show_modal(id) {
    group_modal.show();
}

function hide_modal(id) {
    group_modal.hide();
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
