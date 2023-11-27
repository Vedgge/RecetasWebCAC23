document.addEventListener('DOMContentLoaded', function () {
    const modals = document.querySelectorAll('.contenedor-modal-popup');
    const overlay = document.querySelector('.overlay');

    function mostrarModal(modal) {
        modal.style.display = (modal.style.display === 'block') ? 'none' : 'block';
    }

    function esconderOtroModal(actualModal) {
        modals.forEach(modal => {
            if (modal !== actualModal && modal.style.display === 'block') {
                modal.style.display = 'none';
            }
        });
    }

    document.body.addEventListener('click', function (evento) {
        const target = evento.target;
        if (target.classList.contains('cerrar-btn')) {
            modals.forEach(modal => modal.style.display = 'none');
        } else if (target.id === 'mostrar-modal-login') {
            const loginModal = document.querySelector('.login-popup');
            mostrarModal(loginModal);
            esconderOtroModal(loginModal);
        } else if (target.id === 'mostrar-modal-signup') {
            const signupModal = document.querySelector('.signup-popup');
            mostrarModal(signupModal);
            esconderOtroModal(signupModal);
        }
    });

    //OWL CARRUSEL

    var owl = $('.owl-carousel');
    owl.owlCarousel({
        items: 4,
        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true
    });
    $('.play').on('click', function () {
        owl.trigger('play.owl.autoplay', [1000])
    })
    $('.stop').on('click', function () {
        owl.trigger('stop.owl.autoplay')
    })
});