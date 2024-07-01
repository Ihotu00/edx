var _modal;
var _canvas;
var is_canvas = false;

// initialize tootips
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
})

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

// create alerts
function create_alert(parentId, message, type, icon) {
    icon = !icon ? 'notifications' : icon
    console.log(icon)
    const alertPlaceholder = document.getElementById(parentId)
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div class="d-flex"><span class="material-symbols-outlined me-1">${icon}</span> ${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertPlaceholder.append(wrapper)
}

function create_post() {
    // event.preventDefault();
    show("create-post-loader")
    hide("create-post-button")
    console.log(JSON.stringify({
        'group_name': document.getElementById('post-receiver').value != null ? document.getElementById('post-receiver').value : null,
        'post_body': document.getElementById('post-body').value,
        'type': 'new'
    }))
    // $.ajax({
    //     url: `/post/submit/new`,
    //     type: 'POST',
    //     contentType: 'application/json',
    //     data: JSON.stringify({
    //         'group_name': document.getElementById('post-receiver').value != null ? document.getElementById('post-receiver').value : null,
    //         'post_body': document.getElementById('post-body').value,
    //         'type': 'new'
    //     }),
    //     success: function(response) {
    //         console.log(response)
    //     },
    //     error: function(error) {
    //         console.log(error);
    //         hide("create-post-loader")
    //         show("create-post-button")
    //         create_alert('create-post-response', `${error.responseText}`, 'danger', 'error')
    //     }
    // });
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
    show('create-group-loader')
    hide('submit-new-group')
    group = {
        'group_name': document.getElementById('group_name').value,
        'group_photo': document.getElementById('group_photo').src != "" ? document.getElementById('group_photo').src : null,
        'access': document.getElementById('public-group').checked ? "public" : "private",
    }
    console.log(group)
    $.ajax({
        url: '/create/group',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(group),
        success: function(response) {
            console.log(response)
            location.pathname = response;
        },
        error: function(error) {
            hide('create-group-loader')
            show('submit-new-group')
            console.log(error.responseText);
            create_alert('create-group-response', `${error.responseText}`, 'danger', 'error')
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
            create_alert("login-response", `${error.responseText}`, 'danger', 'error')
            hide("spinner")
            document.getElementById("submit-form").classList.remove("disabled")
        }
    });
}

function imageUploaded(event, id) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file)
    reader.onloadend = () => {
        document.getElementById(id).src = reader.result
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
