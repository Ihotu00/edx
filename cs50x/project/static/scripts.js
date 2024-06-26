var _modal;
var _canvas;
var is_canvas = false;

// initialize tootips
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
})

// document.getElementById("post-link").setAttribute("onClick", "show_header()")

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

function send_post(event) {
    event.preventDefault();
    show("spinner")
    document.getElementById("submit-post").classList.add("disabled")
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
        },
        complete: function() {
            hide("spinner")
            document.getElementById("submit-post").classList.remove("disabled")
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

function login(event, url) {
    event.preventDefault();
    show("spinner")
    document.getElementById("submit-form").classList.add("disabled")
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'username': event.target.username.value,
            'password': event.target.password.value,
            'confirmation': url == "/register" ? event.target.confirmation.value : "",
            'photo': url == "/register" ? event.target.photo.src : ""
        }),
        success: function(response) {
            location.pathname = `/feed/user/${event.target.username.value}`;
        },
        error: function(error) {
            console.log(error)
            show("error-response")
            document.getElementById('error-response').innerHTML = error.responseText
            hide("spinner")
            document.getElementById("submit-form").classList.remove("disabled")
        }
    });
}

function imageUploaded(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file)
    reader.onloadend = () => {
        document.getElementById("display_profile_picture").src = reader.result
    };
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
