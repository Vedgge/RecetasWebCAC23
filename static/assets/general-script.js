document.addEventListener('DOMContentLoaded', function () {
    const modals = document.querySelectorAll('.contenedor-modal-popup');
    const overlay = document.querySelector('.overlay');

    function mostrarModal(modal) {
        modal.style.display = 'block';
        overlay.style.display = 'block';
    }

    function esconderModal(modal) {
        modal.style.display = 'none';
        overlay.style.display = 'none';
    }

/**
 * Oculta todos los modales, excepto el modal actual.
 * @param {HTMLElement} actualModal - El modal actual que no se debe ocultar.
 */
function esconderOtroModal(actualModal) {
    // Itera sobre todos los modals
    modals.forEach(modal => {
        // Verifica si el modal no es el actual y está visible
        if (modal !== actualModal && modal.style.display === 'block') {
            // Oculta el modal
            esconderModal(modal);
        }
    });
}

    // Manejo de eventos para clics en el body
    document.body.addEventListener('click', function (evento) {
        // Obtiene el elemento que fue clickeado
        const target = evento.target;

        // Cierra todos los modales al hacer clic en el botón de cerrar
        if (target.classList.contains('cerrar-btn')) {
            modals.forEach(modal => {
                esconderModal(modal);
            });
        }
        // Muestra el modal de inicio de sesión y oculta otros modales
        else if (target.id === 'mostrar-modal-login') {
            const loginModal = document.querySelector('.login-popup');
            mostrarModal(loginModal);
            esconderOtroModal(loginModal);
        }
        // Muestra el modal de registro y oculta otros modales
        else if (target.id === 'mostrar-modal-signup') {
            const signupModal = document.querySelector('.signup-popup');
            mostrarModal(signupModal);
            esconderOtroModal(signupModal);
        }
        // Oculta el modal de inicio de sesión y muestra el modal de registro
        else if (target.id === 'registrar') {
            const loginModal = document.querySelector('.login-popup');
            const signupModal = document.querySelector('.signup-popup');
            esconderModal(loginModal);
            mostrarModal(signupModal);
        }
        // Oculta el modal de registro y muestra el modal de inicio de sesión
        else if (target.id === 'iniciar-sesion') {
            const loginModal = document.querySelector('.login-popup');
            const signupModal = document.querySelector('.signup-popup');
            esconderModal(signupModal);
            mostrarModal(loginModal);
        }
    });

    //Owl carrusel
    var owl1 = $("#carrusel-1");
    owl1.owlCarousel({
        items: 4,
        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true
    });
    $('.play').on('click', function () {
        owl1.trigger('play.owl.autoplay', [1000])
    })
    $('.stop').on('click', function () {
        owl1.trigger('stop.owl.autoplay')
    })

    var owl2 = $("#carrusel-2");
    owl2.owlCarousel({
        loop: true,
        nav: true,
        margin: 20,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        // itemsDesktop : [1499,4],
        // itemsDesktopSmall : [1199,3],
        // itemsTablet : [899,2],
        // itemsMobile : [599,1],
        // navigation : true,
        // navigationText : ['<span class="fa-stack"><i class="fa fa-circle fa-stack-1x"></i><i class="fa fa-chevron-circle-left fa-stack-1x fa-inverse"></i></span>','<span class="fa-stack"><i class="fa fa-circle fa-stack-1x"></i><i class="fa fa-chevron-circle-right fa-stack-1x fa-inverse"></i></span>'],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            960: {
                items: 5
            },
            1200: {
                items: 6
            }
        }
    });
    owl2.on('mousewheel', '.owl-stage', function (e) {
        if (e.deltaY > 0) {
            owl2.trigger('next.owl');
        } else {
            owl2.trigger('prev.owl');
        }
        e.preventDefault();
    });
});