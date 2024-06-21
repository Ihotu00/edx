var _modal;

function hide(id) {
    document.getElementById(id).classList.add('hide');
}


function show(id) {
    document.getElementById(id).classList.remove('hide');
}

function show_modal(id) {
    _modal = new bootstrap.Modal(document.getElementById(id))
    _modal.show();
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
            console.log(`success: ${JSON.stringify(response)}`);
            _modal.hide();
            let child = `<button class="nav-link" id="${response["id"]}" data-bs-toggle="pill" data-bs-target="#v-pills-home"
                type="button" role="tab" aria-controls="v-pills-home" aria-selected="true"
                onClick='selected(${response})'>${ response["group_name"] }</button>`;
            document.getElementById('group-parent-div').insertAdjacentHTML( 'afterbegin', child );
            selected(response);
        },
        error: function(error) {
            console.log(error.responseText);
            show("group-taken");
        }
    });
}


//  offcanvas offcanvas-start off-canvas-lg show
function canvas() {
    document.getElementByid('group-parent-div').classList.add('offcanvas')
    document.getElementByid('group-parent-div').classList.add('offcanvas-start')
}
