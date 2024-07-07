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

function create_post(event, type, id) {
    console.log(event)
    event.preventDefault();
    show(event.target.loader_button.id)
    hide(event.target.submit_button.id)
    $.ajax({
        url: id != null ? `/post/submit?id=${id}` : `/post/submit`,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'post_body': event.target.post_body.value,
            'type': type
        }),
        success: function(response) {
            location.pathname = `/post`;
            location.search = `?id=${response}`
        },
        error: function(error) {
            console.log(error);
            hide(event.target.loader_button.id)
            show(event.target.submit_button.id)
            create_alert(event.target.parentNode.querySelector("[name='response']").id, `${error.responseText}`, 'danger', 'error')
        }
    });
}

function vote_on_post(vote, id) {
    console.log(vote)
    // const params = new URLSearchParams(location.search)
    // id = params.get('id')
    document.getElementById("vote-loader").classList.add('d-flex')
    show("vote-loader")
    document.getElementById("vote-buttons").classList.remove('d-flex')
    hide("vote-buttons")
    $.ajax({
        url: `/vote?id=${id}`,
        type: 'POST',
        data: {'vote': vote},
        success: function(response) {
            document.getElementById("vote-loader").classList.remove('d-flex')
            hide("vote-loader")
            document.getElementById("vote-buttons").classList.add('d-flex')
            show("vote-buttons")
            document.getElementById("total-votes").innerHTML = response
        },
        error: function(error) {
            document.getElementById("vote-loader").classList.remove('d-flex')
            hide("vote-loader")
            document.getElementById("vote-buttons").classList.add('d-flex')
            show("vote-buttons")
            create_alert("vote-response", `${error.responseText}`, 'danger', 'error')
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
            location.pathname = `/`;
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
