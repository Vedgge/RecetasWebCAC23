document.addEventListener('DOMContentLoaded', function(){
    const modals = document.querySelectorAll('.cancelar-popup');
    const overlay = document.querySelector('.overlay-cancelar');

    function mostrarModal(modal) {
        modal.style.display = 'block';
        overlay.style.display = 'block'; 
    }

    function esconderModal(modal) {
        modal.style.display = 'none';
        overlay.style.display = 'none'; 
    }

    document.body.addEventListener('click', function (evento) {
        const target = evento.target;
        if (target.classList.contains('cerrar-btn')) {
            modals.forEach(modal => esconderModal(modal));
        } else if (target.id === '#mostrar-modal-cancelar') {
            evento.preventDefault();
            const cancelarPopup = document.querySelector('.cancelar-popup');
            mostrarModal(cancelarPopup);
            esconderOtroModal(cancelarPopup);
        } else if (target.classList.contains('cancelar-popup') || target.tagName === 'BUTTON') {
            const cancelarPopup = document.querySelector('.cancelar-popup');
            esconderModal(cancelarPopup);
        }
    });
});
