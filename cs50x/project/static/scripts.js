var _modal;
var _canvas;
var is_canvas = false;

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
    get_posts(group["group_id"]);
    document.getElementById('group_header').innerHTML = group["group_name"];
    document.getElementById('group_id').value = group["group_id"];
    if (is_canvas) close_canvas();
}


function send_post() {
    $.ajax({
        url: '/post',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'group_id': document.getElementById('group_id').value,
            'message': document.getElementById('post').value
        }),
        success: function(response) {
            console.log(`success: ${JSON.stringify(response)}`);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function get_posts(id) {
    $.ajax({
        url: '/post?group_id=' + id,
        type: 'GET',
        success: function(response) {
            header = document.getElementById("group_posts")
            header.replaceChildren();
            for (x = 0; x < response.length; x++) {
                header.insertAdjacentHTML('beforeend',
                    `<h1 id="group_header">${response[x]["group_name"]}</h1>
                    <div class="card mt-5 text-bg-primary">
                        <div class="card-header"></div>
                        <div class="card-body">
                            ${response[x]["post"]}
                        </div>
                        <div class="card-footer text-end">
                            ${response[x]["creation_time"]}
                        </div>
                    </div>`);
            }
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
        data: JSON.stringify({ 'group_name': document.getElementById('group_name').value }),
        success: function(response) {
            console.log(`success: ${JSON.stringify(response)}`);
            _modal.hide();
            let child = `<div class="card mt-3 text-bg-primary" onClick="selected(${response})">
                            <div class="card-body">
                            ${response["group_name"]}
                            </div>
                        </div>`;
            document.getElementById('add-group-button').insertAdjacentHTML('beforebegin', child);
            selected(response);
        },
        error: function(error) {
            console.log(error.responseText);
            show("group-taken");
        }
    });
}


function show_canvas() {
    document.getElementById('close-canvas').classList.remove('hide');
    document.getElementById('group-parent-div').classList.remove('d-none');
    document.getElementById('group-parent-div').classList.add('offcanvas');
    document.getElementById('group-parent-div').classList.add('offcanvas-start');
    document.getElementById('group-parent-div').style['max-height'] = '100%';
    _canvas = new bootstrap.Offcanvas('#group-parent-div');
    _canvas.show();
    is_canvas = true;
}

function close_canvas() {
    _canvas.hide();
    document.getElementById('close-canvas').classList.add('hide');
    document.getElementById('group-parent-div').classList.add('d-none');
    document.getElementById('group-parent-div').classList.remove('offcanvas');
    document.getElementById('group-parent-div').classList.remove('offcanvas-start');
    document.getElementById('group-parent-div').style['max-height'] = '300px';
}
