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

function send_post() {
    group_id;
    element = "posts";
    position = "afterbegin"
    if (document.getElementById('groups-tab-pane').classList.contains("show")) {
        group_id = document.getElementById('group_id').value
        position = "afterend";
        element = "group_header";
    }
    $.ajax({
        url: '/post',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'group_id': group_id,
            'message': document.getElementById('post').value
        }),
        success: function(response) {
            no_posts_msg = document.getElementById('no_posts_msg');
            if (no_posts_msg) { no_posts_msg.remove(); }
            document.getElementById(element).insertAdjacentHTML(position,
                `<div class="card mt-5 text-bg-primary">
                    <div class="card-header text-start">
                        <img src=${response["photo"]} style="clip-path: circle();" width="20" height="20">
                        ${response["username"]}
                    </div>
                    <div class="card-body">
                        ${response["post"]}
                    </div>
                    <div class="card-footer text-end">
                        ${response["creation_time"]}
                    </div>
                </div>`);
            document.getElementById('post').value = '';
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function get_group_msg(id, name) {
    document.getElementById('group_id').value = id;
    header = document.getElementById("group_posts")
    header.replaceChildren();
    header.insertAdjacentHTML('beforeend', `<h1 id="group_header" class="sticky-top bg-dark">${name}</h1>`)
    $.ajax({
        url: '/post?group_id=' + id,
        type: 'GET',
        success: function(response) {
            for (x = 0; x < response.length; x++) {
                header.insertAdjacentHTML('beforeend',
                    `<div class="card mt-5 text-bg-primary">
                        <div class="card-header text-start">
                            <img src=${response[x]["photo"]} style="clip-path: circle()" width="20" height="20">
                            ${response[x]["username"]}
                        </div>
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
            if (error.status == 404) {
                console.log(error)
                header.insertAdjacentHTML('beforeend',
                    `<div class="center" id="no_posts_msg">
                        <h1 class="text-white-50" style="font-size: 15cqb; color: white">${error.responseText}</h1>
                    </div>`)
            }
        }
    });
    if (is_canvas) close_canvas();
}

function create_group() {
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

function login() {
    $.ajax({
        url: '/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'username': document.getElementById('username').value,
            'password': document.getElementById('password').value }),
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
