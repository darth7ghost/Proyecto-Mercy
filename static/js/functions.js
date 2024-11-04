document.addEventListener('DOMContentLoaded', function () {
    const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

    // Función para marcar el item activo
    function setActiveMenuItem() {
        allSideMenu.forEach(item => {
            const li = item.parentElement;
            item.addEventListener('click', function () {
                allSideMenu.forEach(i => {
                    i.parentElement.classList.remove('active');
                });
                li.classList.add('active');
                // Guardar el estado activo en localStorage
                localStorage.setItem('activeMenu', item.getAttribute('href'));
            });
        });
    }

    // Función para restaurar el item activo al cargar la página
    function restoreActiveMenuItem() {
        const activeMenu = localStorage.getItem('activeMenu');
        if (activeMenu) {
            allSideMenu.forEach(item => {
                const li = item.parentElement;
                if (item.getAttribute('href') === activeMenu) {
                    li.classList.add('active');
                } else {
                    li.classList.remove('active');
                }
            });
        }
    }

    setActiveMenuItem();
    restoreActiveMenuItem();

    // Seleccionar el enlace de logout y eliminar el estado del menú lateral en localStorage
    const logoutLink = document.querySelector('.side-menu .logout');
    if (logoutLink) {
        logoutLink.addEventListener('click', function () {
            localStorage.removeItem('activeMenu');
        });
    }
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector('.content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})


const searchButton = document.querySelector('.content nav form .form-input button');
const searchButtonIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');


if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchForm.classList.remove('show');
	}
})

document.addEventListener('DOMContentLoaded', function () {
    // Obtener el interruptor de modo
    const switchMode = document.getElementById('switch-mode');
    
    // Recuperar la preferencia del tema del localStorage
    const currentTheme = localStorage.getItem('theme');
    
    // Aplicar el tema guardado si existe
    if (currentTheme) {
        document.body.classList.add(currentTheme);

        // Si el tema es oscuro, marcar el interruptor como checked
        if (currentTheme === 'dark') {
            switchMode.checked = true;
        }
    }

    // Añadir un evento para cambiar el tema y guardar la preferencia en localStorage
    switchMode.addEventListener('change', function () {
        if (this.checked) {
            document.body.classList.add('dark');
            localStorage.setItem('theme', 'dark');  // Guardar la preferencia
        } else {
            document.body.classList.remove('dark');
            localStorage.setItem('theme', 'light');  // Guardar la preferencia
        }
    });
});
/*
function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}

function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        console.log(data);
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}

function alert_action(title, content, callback, cancel) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    callback();
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    cancel();
                }
            },
        }
    })
}
*/